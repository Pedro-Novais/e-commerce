from repository._UserRepository import UserRepository

from custom_exceptions._CustomExceptions import NotFoundError



class GetUser:
    def __init__(self, userId) -> str:
        self.id = userId

    def action(self):
        user_repo = UserRepository()

        user = user_repo.get_user_by_id(user_id=self.id)

        if not user:
            raise NotFoundError("Usuário não foi encontrado!")
        
        data = {
            "name": user.name,
            "email": user.email,
            "is_admin": user.is_admin,
            "created_at": user.created_at.strftime("%d/%m/%Y")
        }
        return data