from utils._I18nShared import I18nShared
from ._I18n import I18n

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
            raise NotFoundError(I18n.NOT_FOUND_USER)

        if user.is_admin:
            raise AdminCanotBeDeletedError()

        delete_user = user_repo.delete(id=self.id, shop=self.shop)

        if delete_user == I18nShared.ANY_DATA:
            raise OperationError(I18n.ERROR_DELETE_USER)

        return I18n.SUCCESS_DELETE_USER