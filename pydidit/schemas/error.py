




from pydantic import BaseModel


class AuthenticationError(BaseModel):
    
    detail:str #Error message
    status_code:int | None = None #HTTP status code