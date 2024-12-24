from flask import Request, Response

from repository._UserRepository import UserRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    AdminCanotBeDeletedError
)


class DeleteUser:
    def __init__(self, userId):
        self.id = userId

    def action(self):
        user_repo = UserRepository()

        user = user_repo.get_user_by_id(user_id=self.id)

        if not user:
            raise NotFoundError("Usuário não encontrado")

        if user.is_admin:
            raise AdminCanotBeDeletedError()

        delete_user = user_repo.delete_user(user_id=self.id)

        return "Usuário deletado com sucesso"