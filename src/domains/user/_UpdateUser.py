from flask import Request

class UpdateUser:
    def __init__(self, request: Request, userId: int):
        self.request = request

    def action(self):
        pass