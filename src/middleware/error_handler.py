from flask import jsonify
from custom_exceptions._CustomError import CustomError

def error_handler(error):
    if isinstance(error, CustomError):
        response = {}

        if error.msg_error:
            response = {
                "message": str(error.message),
                "error": str(error.msg_error),
            }
        else:
            response = {
                "message": str(error.message)
            }
            
        return jsonify(response), error.status_code
    
    response = {"message": "Internal server error", "error": str(error)}
    return jsonify(response), 500
