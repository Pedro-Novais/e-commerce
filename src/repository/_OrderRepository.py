from datetime import datetime

from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.OrderModel import Order

class OrderRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Order,
            conn=self.conn
        )

    def create_order(
            self,
            user_id:int,
            address_id:int,
            shop:str,
            total_price:int,
            delivery_date: datetime = None, 
            shipment_tracking_number: str = None,
            shipping_fee: float = 0.00,
            discount: float = 0.00,
            tax: float = 0.00,
            cancellation_reason: str = "",
            status: str = "PENDING"
            ):
        with self.conn.get_db_session() as db:
            
            new_order = Order(
                user_id = user_id,
                address_id = address_id,
                shop_name = shop,
                total_price = total_price,
                discount = discount,
                tax = tax,
                shipping_fee = shipping_fee,
                shipment_tracking_number = shipment_tracking_number,
                delivery_date = delivery_date,
                cancellation_reason=cancellation_reason,
                status = status
            )

            db.add(new_order)
            db.commit()
            db.refresh(new_order)
            return new_order