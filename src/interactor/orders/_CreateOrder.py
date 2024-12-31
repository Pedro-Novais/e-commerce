from flask import Request

from service import CreatePaymentService

from utils._I18nShared import I18nShared
from ._I18n import I18n

from repository.Conn import ConnDatabase
from repository._UserRepository import UserRepository
from repository._OrderRepository import OrderRepository
from repository._ProductVariantsRepository import ProductVariantsRepository
from repository._PaymentRepository import PaymentRepositoy

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    ParameterNotSend,
    OperationError,
    )

class CreateOrder:
    def __init__(self, shop_name: str, request: Request, user_id: int = None):
        self.user_id = user_id
        self.shop = shop_name
        self.conn = ConnDatabase()
        
        request = request.get_json()
        
        self.validators_data(request=request)

    def action(self):
        with self.conn.get_db_session() as db:
            order_repo = OrderRepository()
            product_variant_repo = ProductVariantsRepository()
            payment_repo = PaymentRepositoy()

            self.verify_integrity_items(repo=product_variant_repo, items=self.items)

            new_order = order_repo.create_order(
                db=db,
                user_id=self.user_id,
                address_id=self.address_id,
                shop=self.shop,
                total_price=self.transaction_amount,
                shipping_fee=self.shipping_fee,
                discount=self.discount,
                payer_email=self.payer_email,
                payer_address=self.payer_address,
                items=self.items
            )

            payment_data = self.create_request_data()

            payment_service = CreatePaymentService(payment_data=payment_data)
            status_request, response, status_code = payment_service.action()

            if status_request == I18nShared.ANY_DATA:
                MESSAGE_ERROR_REQUEST = payment_service.verify_status_transaction_error(response=response)
                raise OperationError(MESSAGE_ERROR_REQUEST)

            STATUS_ORDER, STATUS_OK, STATUS_DETAIL = payment_service.verify_status_transaction_success(response=response)

            new_payment = payment_repo.create_payment(
                db=db,
                order_id=new_order.id,
                shop=self.shop,
                payment_method=payment_data["payment_method_id"],
                status=I18n.STATUS_ORDER_NEW,
                transaction_id=response.get("id")
            )
                
            if not new_payment:
                raise OperationError(I18n.ERROR_CREATE_PAYMENT)

            new_order.status = STATUS_ORDER
            new_order.reason = STATUS_DETAIL
            db.commit()

            if not STATUS_OK == "APPROVED":
                raise OperationError(I18n.ERROR_PROCESSING_PAYMENT.format(reason=STATUS_DETAIL))
            
            return I18n.SUCCESS_CREATE_ORDER
    
    def create_request_data(self):
        user_repo = UserRepository()

        user_email = None

        if self.user_id:
            user = user_repo.get_by_id(id=self.user_id, shop=self.shop)
            user_email = user.email
            if not user:
                raise NotFoundError()
        else:
            user_email = self.payer_email

        payer_data = {
                "email": user_email,
                "identification": {
                "type": "CPF",  
                "number": "12345678909"  
                    }
                }
        
        payment_data = {
            "transaction_amount": self.transaction_amount,
            "token": self.token_card,
            "description": self.description,
            "installments": self.installments,  
            "payment_method_id": self.payment_method,
            "payer": payer_data
        }

        return payment_data

    def validators_data(self, request):
        self.transaction_amount = request.get("transaction_amount", None)
        if not self.transaction_amount or self.transaction_amount == 0 or not isinstance(self.transaction_amount, float):
            raise ParameterNotSend()

        self.token_card = request.get("token_card", None)
        if not self.token_card:
            raise ParameterNotSend()

        self.description = request.get("description", "")

        self.payment_method = request.get("payment_method", None)
        if not self.payment_method or not self.payment_method in ["PIX", "visa", "master"]:
            raise ParameterNotSend()
        
        self.payer_email = None
        self.payer_address = None
        self.address_id = None
        if not self.user_id:
            self.payer_email = request.get("payer_email", None)
            self.payer_address = request.get("payer_address", None)

            if not self.payer_email:
                raise ParameterNotSend()
            if not self.payer_address:
                raise ParameterNotSend()
        else:
            self.address_id = request.get("address_id", None)
            if not self.address_id:
                raise ParameterNotSend()
            
        self.items = request.get("items", None)
        if not self.items:
            raise ParameterNotSend()
        
        for item in self.items:
            if not item.get("id"):
                raise ParameterNotSend()
            if not item.get("quantity"):
                raise ParameterNotSend()
            if not item.get("price"):
                raise ParameterNotSend()
        
        self.shipping_fee = request.get("shipping_fee", None)
        if not self.shipping_fee:
            raise ParameterNotSend()
        
        self.discount = request.get("discount", 0)

        self.installments = request.get("installments", 1)

    def verify_integrity_items(self, repo, items):
        item_integrity = repo.get_items_from_order(items=items)
        if not item_integrity:
            raise NotFoundError(I18n.NOT_FOUND_PRODUCTS_FROM_ORDER)