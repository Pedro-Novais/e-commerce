from flask import jsonify
from custom_exceptions._CustomError import CustomError

def error_handler(error):
    if isinstance(error, CustomError):
        response = {}

        if error.msg_error:
            response = {
                "msg": str(error.message),
                "error": str(error.msg_error),
            }
        else:
            response = {
                "msg": str(error.message)
            }
            
        return jsonify(response), error.status_code
    
    response = {"msg": "Internal server error", "error": str(error)}
    return jsonify(response), 500
