from datetime import datetime

from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.OrderModel import Order
from model.OrderItemModel import OrderItem

class OrderRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Order,
            conn=self.conn
        )

    def create_order(
            self,
            db,
            user_id:int,
            address_id:int,
            shop:str,
            total_price:int,
            payer_email: str = None,
            payer_address: list = None,
            delivery_date: datetime = None, 
            shipment_tracking_number: str = None,
            shipping_fee: float = 0.00,
            discount: float = 0.00,
            tax: float = 0.00,
            reason: str = "",
            status: str = "PENDING",
            items: list = []
            ):
       
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
            reason=reason,
            status = status,
            payer_email = payer_email,
            payer_address = payer_address
        )

        db.add(new_order)
        db.flush()

        for item in items:
            new_order_item = OrderItem(
                order_id=new_order.id,
                product_variant_id=item.get("id"),
                shop_name=shop,
                quantity=item.get("quantity"),
                price=item.get("price")
            )

            db.add(new_order_item)
            db.flush()  

        db.refresh(new_order)
        return new_order