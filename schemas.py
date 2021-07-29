from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

class Otp_email(BaseModel):
    email: str
    otp: str
    
class User(BaseModel):
    user_email: str
    password: str
    user_name: str
    user_city: str


class Log_in(BaseModel):
    username: str
    password: str


class user_model(BaseModel):
    user_email: str
    user_name: str
    user_city: str

    class Config():
        orm_mode = True
