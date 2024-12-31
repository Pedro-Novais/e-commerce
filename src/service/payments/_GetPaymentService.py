import os
import uuid
import mercadopago

from utils._I18nShared import I18nShared
from ._StatusCodeResponse import StatusCodeResponse
from dotenv import load_dotenv

class GetPaymentService:

    def __init__(
            self,
            transaction,
            access_token
            ):
        load_dotenv()
        self.sdk = mercadopago.SDK(os.getenv("ACCESS_TOKEN"))
        self.idempotency_key = str(uuid.uuid4())

        self.transaction = transaction

    def action(self):

        payment_response = self.sdk.payment().get(payment_id=self.transaction)

        if not payment_response["status"] in [200, 201]:
                return I18nShared.ANY_DATA, payment_response["response"], payment_response["status"]
        
        return I18nShared.WITH_DATA, payment_response["response"], payment_response["status"]
