from ._I18n import I18n

from repository._UserRepository import UserRepository

from custom_exceptions._CustomExceptions import NotFoundError

class GetUser:
    def __init__(self, userId: int, shop_name: str) -> str:
        self.id = userId
        self.shop = shop_name

    def action(self):
        user_repo = UserRepository()

        user = user_repo.get_user_by_id(user_id=self.id, shop=self.shop)

        if not user:
            raise NotFoundError(I18n.NOT_FOUND_USER)
        
        data = {
            "name": user.name,
            "email": user.email,
            "is_admin": user.is_admin,
            "created_at": user.created_at.strftime("%d/%m/%Y"),
            "address": [
                {
                    "street": address.street,
                    "number": address.number,
                    "city": address.city,
                    "state": address.state,
                    "zip_code": address.zip_code,
                    "country": address.country
                } for address in user.addresses
            ]
        }
        return data