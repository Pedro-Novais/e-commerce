import os

from flask import jsonify
from functools import wraps
from sqlalchemy.orm.exc import NoResultFound

from custom_exceptions._CustomExceptions import OperationError

from dotenv import load_dotenv

def handle_webhook_auth_panel(f):
    @wraps(f)
    def decorated(*args, **kwargs): 
        try:
            load_dotenv()
            subdomain = kwargs.get('subdomain')

            if not subdomain == os.getenv("SUBDOMAIN_MAJOR"):
                raise OperationError("Ação não permitida!")

        except NoResultFound:
            return jsonify({"error": "Usuário não encontrado no banco de dados."}), 404

        except Exception as err:
            return jsonify({"msg": "Erro inesperado durante a validação de administrador.", "error": str(err)}), 500

        return f(*args, **kwargs)

    return decorated
