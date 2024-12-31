from flask import Request

from utils._I18nShared import I18nShared
from ._I18n import I18n

from service import GetPaymentService
from repository._PaymentRepository import PaymentRepositoy

class WebHookOrder:
    def __init__(self, request: Request):
        request = request.get_json()
        self.transaction_id = request.get("data").get("id", None)

    def action(self):
        payment_service = GetPaymentService(transaction=self.transaction_id)
        payment_repo = PaymentRepositoy()

        payment_internal = payment_repo.get_payment(id=self.transaction_id)
        STATUS, RESPONSE, STATUS_CODE = payment_service.action()

        if STATUS == I18nShared.ANY_DATA:
            raise

        new_status_payment = RESPONSE.get("status")
        return new_status_payment