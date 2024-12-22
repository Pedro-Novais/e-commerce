import jwt
import os

from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        load_dotenv()
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1] if len(auth_header.split(" ")) > 1 else None

        if not token:

            response = {
                'message': 'Acesso Negado!' 
            }
            
            return jsonify(response), 401
        
        try:
            data = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])
            userId = data['user_id']

        except ExpiredSignatureError:
            return jsonify({"error": "Token expirado. Por favor, faça login novamente."}), 401
        
        except InvalidTokenError:
            return jsonify({"error": "Token inválido."}), 401

        except Exception as err:

            response = {
                'message': 'Acesso Negado!',
                'error': str(err) 
            }

            return jsonify(response), 401
        
        return f(userId, *args, **kwargs)
    
    return decorated