from repository._ProductRepository import ProductRepository

from custom_exceptions._CustomExceptions import (
    ParameterNotSend,
    OperationError
)

class DeleteProduct:
    def __init__(self, product_id: int):
        self.product_id = product_id

        if not self.product_id:
            raise ParameterNotSend("Paramêtros obrigatórios não foram enviados!")
        
    def action(self):
        product_repo = ProductRepository()

        delete_product = product_repo.delete(id=self.product_id)

        if not delete_product:
            raise OperationError("Erro ao deletar produto!")
        
        if delete_product == "AnyData":
            raise OperationError("Produto não foi encontrado para ser deletado!")

        return "Produto deletado com sucesso"