class CustomError(Exception):
    def __init__(self, message: str, status_code: int = 500, msg_error: str = ""):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.msg_error = msg_error