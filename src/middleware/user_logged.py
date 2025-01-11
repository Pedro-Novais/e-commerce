from flask import request, jsonify
from functools import wraps
from sqlalchemy.orm.exc import NoResultFound

from utils._I18nShared import I18nShared
from repository._UserRepository import UserRepository

def handle_user_logged(f):
    @wraps(f)
    def decorated(*args, **kwargs): 
        try:
            # token = None 
            token = request.cookies.get('authToken')
            info_user_logged = I18nShared.USER_LOGGED

            # if 'Authorization' in request.headers:
            #     auth_header = request.headers['Authorization']
                # token = auth_header.split(" ")[1] if len(auth_header.split(" ")) > 1 else None

            if not token:
                info_user_logged = I18nShared.USER_NOT_BE_LOGGED

        except Exception as err:
            return jsonify({"msg": I18nShared.INTERNAL_SERVER_ERROR, "error": str(err)}), 500

        return f(info_user_logged, *args, **kwargs)

    return decorated
