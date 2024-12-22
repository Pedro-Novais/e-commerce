from ._CustomError import CustomError

class InfoAlreadyInUseError(CustomError):
    def __init__(self, message: str = "Informação já está cadastrada"):
        super().__init__(message, status_code=400)

class FormatInvalidError(CustomError):
    def __init__(self, message: str = "Paramêtros invalidos enviados"):
        super().__init__(message, status_code=400)

class NotFoundError(CustomError):
    def __init__(self, message: str = "Recurso não encontrado"):
        super().__init__(message, status_code=404)

class CredentialIncorrectError(CustomError):
    def __init__(self, message: str = "Credenciasi invalídas!"):
        super().__init__(message, status_code=400)
        
class AdminCanotBeDeletedError(CustomError):
    def __init__(self, message: str = "Usuário niveis admin não podem ser excluídos!"):
        super().__init__(message, status_code=400)

class OperationError(CustomError):
    def __init__(self, message: str = "Erro ao realizar operação!", error: str = ""):
        super().__init__(message, status_code=400, msg_error = error)