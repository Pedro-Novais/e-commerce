from flask import Request, Response

from repository._UserRepository import UserRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    OperationError,
    AdminCanotBeDeletedError
)


class DeleteUser:
    def __init__(self, userId: int, shop_name: str):
        self.id = userId
        self.shop = shop_name

    def action(self):
        user_repo = UserRepository()

        user = user_repo.get_user_by_id(user_id=self.id, shop=self.shop)

        if not user:
            raise NotFoundError("Usuário não encontrado")

        if user.is_admin:
            raise AdminCanotBeDeletedError()

        delete_user = user_repo.delete(id=self.id, shop=self.shop)

        if delete_user == "AnyData":
            raise OperationError("Erro ao excluir conta!")

        return "Usuário deletado com sucesso"