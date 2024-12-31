from flask import Request

from utils._I18nShared import I18nShared
from ._I18n import I18n

from service import (
    GetPaymentService,
    StatusCodeResponse
)

from repository.Conn import ConnDatabase
from repository._PaymentRepository import PaymentRepositoy
from repository._NotificationRepository import NotificationRepository

class WebHookOrder:
    def __init__(self, request: Request):
        self.conn = ConnDatabase()
        self.request = request.get_json()

        self.notification_id = self.request.get("id")
        self.transaction_id = self.request.get("data").get("id", None)
        
        if not self.transaction_id:
            raise

    def action(self):
        payment_repo = PaymentRepositoy()
        notification_repo = NotificationRepository()

        with self.conn.get_db_session() as db:
            payment_internal = payment_repo.get_payment(db=db, id=self.transaction_id)

            if not payment_internal:
                raise
        
            new_notification = self.create_notification_retry(db=db, shop=payment_internal.shop.name,notification_repo=notification_repo)

            STATUS, RESPONSE, STATUS_CODE = GetPaymentService(transaction=self.transaction_id, access_token=None).action()

            if STATUS == I18nShared.ANY_DATA:
                raise

            status_update = self.update_payment_status(
                actual_status=payment_internal.status,
                new_status=RESPONSE.get("status")                
                )


            if not status_update:
                raise
            else:
                notification_repo.update_notification(db=db,notification=new_notification, processed=status_update)
                payment_repo.update_status_payment(db=db, payment=payment_internal, status=status_update)
            
            return "Status do pagamento alterado"
    
    def update_payment_status(self, actual_status, new_status):
        if new_status:
            if new_status in StatusCodeResponse.SUCCESS: 
                new_status = StatusCodeResponse.SUCCESS[new_status]
                new_status = "APPROVED"
                if actual_status == new_status:
                    return False
                return new_status
            
        return False

    def create_notification_retry(
            self,
            db,
            shop,
            notification_repo
            ):
        
        MAX_RETRIES = 3
    
        for attempt in range(MAX_RETRIES):
            new_notification = notification_repo.create_notification(
                db=db,
                shop=shop,
                notification_id=self.notification_id,
                data=self.request
            )
            
            if new_notification:
                return new_notification

        return False