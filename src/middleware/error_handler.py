from flask import jsonify
from custom_exceptions._CustomError import CustomError

def error_handler(error):
    if isinstance(error, CustomError):
        response = {}

        if error.msg_error:
            response = {
                "message": error.message,
                "error": error.msg_error,
            }
        else:
            response = {
                "message": error.message
            }
            
        return jsonify(response), error.status_code
    
    response = {"message": "Internal server error", "error": error}
    return jsonify(response), 500
