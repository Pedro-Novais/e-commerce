import os
import uuid
import mercadopago

from utils._I18nShared import I18nShared
from ._StatusCodeResponse import StatusCodeResponse
from dotenv import load_dotenv

class CreatePaymentService:

    def __init__(
            self,
            payment_data: dict
            ):
        load_dotenv()
        self.sdk = mercadopago.SDK(os.getenv("ACCESS_TOKEN"))
        self.idempotency_key = str(uuid.uuid4())
        self.payment_data = payment_data

    def action(self):
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': self.idempotency_key
        }

        payment_response = self.sdk.payment().create(payment_object=self.payment_data, request_options=request_options)

        if not payment_response["status"] in [200, 201]:
                return I18nShared.ANY_DATA, payment_response["response"], payment_response["status"]
        
        return I18nShared.WITH_DATA, payment_response["response"], payment_response["status"]
    
    def verify_status_transaction_success(self, response):
        code = response["status"]
        status_detail = response["status_detail"] or ""

        code_msg = "APPROVED"
        detail_msg = "Error"

        if code in StatusCodeResponse.SUCCESS:
            if not code == "approved":
                if code == "pending":
                    code_msg = "Pagamento Pendente"

                elif code == "in_process":
                    code_msg = "Em Processamento"

                elif code == "rejected":
                    code_msg = "Pagamento rejeitado"

                elif code == "cancelled":
                    code_msg = "Pagamento cancelado"
                
                elif code == "authorized":
                    code_msg = "Pagamento autorizado, pendente de confirmação"
            

        if status_detail in StatusCodeResponse.STATUS_DETAIL:
            detail_msg = StatusCodeResponse.STATUS_DETAIL[status_detail]

        return StatusCodeResponse.SUCCESS[code], code_msg, detail_msg
    
    def verify_status_transaction_error(self, response):
         code = response["cause"][0]["code"]
         if code in StatusCodeResponse.ERROR:
              return StatusCodeResponse.ERROR[code]