from flask import jsonify
from functools import wraps
from sqlalchemy.orm.exc import NoResultFound

from repository._UserRepository import UserRepository
from model.UserModel import User

def admin_required(f):
    @wraps(f)
    def decorated(user_id, *args, **kwargs): 
        try:
            user_repo = UserRepository()
            user = user_repo.get_user_by_id(user_id=user_id)

            if not user.is_admin:
                return jsonify({"msg": "Acesso Negado! Permissão de administrador necessária."}), 403

        except NoResultFound:
            return jsonify({"error": "Usuário não encontrado no banco de dados."}), 404

        except Exception as err:
            return jsonify({"msg": "Erro inesperado durante a validação de administrador.", "error": str(err)}), 500

        return f(*args, **kwargs)

    return decorated
