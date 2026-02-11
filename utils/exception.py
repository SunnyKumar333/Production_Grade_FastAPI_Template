class AppError(Exception):
    def __init__(self,message:str,status_code:int):
        self.message:str=message
        self.status_code:int=status_code
        
        
class NotFoundError(AppError):
    def __init__(self,message:str="Resource not found"):
        status_code=404
        super().__init__(message,status_code)
        
class BadRequestError(AppError):
    def __init__(self,message:str="Bad request"):
        message="Bad request"
        status_code=400
        super().__init__(message,status_code)
        
class InternalServerError(AppError):
    def __init__(self,message:str="Internal server error"):
        message="Internal server error"
        status_code=500
        super().__init__(message,status_code)