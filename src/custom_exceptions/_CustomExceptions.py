from utils._I18nShared import I18nShared
from ._CustomError import CustomError

class InfoAlreadyInUseError(CustomError):
    def __init__(self, message: str = I18nShared.INFO_ALREADY_USED):
        super().__init__(message, status_code=400)

class FormatInvalidError(CustomError):
    def __init__(self, message: str = I18nShared.PARAMETER_INVALID):
        super().__init__(message, status_code=400)

class NotFoundError(CustomError):
    def __init__(self, message: str = I18nShared.NOT_FOUND):
        super().__init__(message, status_code=404)

class ParameterNotSend(CustomError):
    def __init__(self, message: str = I18nShared.PARAMETER_NOT_SEND):
        super().__init__(message, status_code=404)

class CredentialIncorrectError(CustomError):
    def __init__(self, message: str = I18nShared.CREDENTIALS_INVALID):
        super().__init__(message, status_code=400)
        
class AdminCanotBeDeletedError(CustomError):
    def __init__(self, message: str = I18nShared.ADMIN_NOT_BE_DELETED):
        super().__init__(message, status_code=400)

class PaymentPending(CustomError):
    def __init__(self, message: str = I18nShared.PAYMENT_PENDING):
        super().__init__(message, status_code=201)

class OperationError(CustomError):
    def __init__(self, message: str = I18nShared.OPERATION_ERROR, error: str = ""):
        super().__init__(message, status_code=400, msg_error = error)