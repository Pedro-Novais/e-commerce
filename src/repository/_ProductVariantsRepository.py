from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.ProductVariantsModel import ProductVariants

class ProductVariantsRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=ProductVariants,
            conn=self.conn
        )