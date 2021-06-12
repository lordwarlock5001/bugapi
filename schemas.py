from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_email:str
    password:str
    user_name:str
    user_city:str
