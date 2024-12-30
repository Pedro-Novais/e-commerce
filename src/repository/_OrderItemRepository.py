from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.OrderItemModel import OrderItem

class OrderItemRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=OrderItem,
            conn=self.conn
        )