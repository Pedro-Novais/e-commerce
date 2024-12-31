from sqlalchemy.orm import joinedload

from model.PaymentsModel import Payment
from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository

class PaymentRepositoy(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Payment,
            conn=self.conn
        )

    def get_payment(self, db, id):
        return db.query(Payment).filter(Payment.transaction_id == id).options(joinedload(Payment.order)).first()

    def create_payment(
            self,
            db,
            order_id,
            shop,
            payment_method,
            status,
            transaction_id,
            paid_at = None
            ):

        new_payment = Payment(
            order_id=order_id,
            shop_name=shop,
            payment_method=payment_method,
            status=status,
            transaction_id=transaction_id,
            paid_at=paid_at
        )

        db.add(new_payment)
        db.flush()
        db.refresh(new_payment)
        return new_payment
    
    def update_status_payment(
            self,
            db, 
            payment,
            status
            ):
        
        payment.status = status

        db.commit()