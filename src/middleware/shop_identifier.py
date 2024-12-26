from flask import jsonify
from functools import wraps
from repository._ShopRepository import ShopRepository
from custom_exceptions._CustomExceptions import NotFoundError
from .error_handler import error_handler

def handle_subdomain(f):
    @wraps(f) 
    def decorator(*args, **kwargs):
       
        subdomain = kwargs.get('subdomain')
        
        if not subdomain:
            return jsonify({"msg":"Acesso negado: subdomínio inválido."}), 403
        
        shop_repo = ShopRepository()

        try:
            shop = shop_repo.get_by_name(name=subdomain)

            if not shop:
                raise NotFoundError("Subdóminio não foi identicado!")
            
            pass
        except (
            Exception,
            NotFoundError
            ) as e:
            return error_handler(error=e)

        return f(*args, **kwargs)
      
    return decorator
