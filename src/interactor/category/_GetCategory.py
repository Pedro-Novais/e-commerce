from flask import Request

from repository._CategoryRepository import CategoryRepository

from custom_exceptions._CustomExceptions import (
    OperationError,
    ParameterNotSend
)

class GetCategory:
    def __init__(self, shop_name: str, request: Request):
        pass

    def action(self):
        pass