from fastapi import APIRouter, Depends, Response, status, HTTPException
from schemas import User, user_model, Log_in
from hashing import create_hash, verify_hash
import models
from database import get_db, session
import token_lib

users_r = APIRouter(
    prefix="/user",
    tags=["User"]
)


@users_r.post("/", response_model=user_model)
def Create_U(request: User, db: session = Depends(get_db), current_user: User = Depends(token_lib.get_current_user)):
    hash_pwd = create_hash(request.password)
    new_user = models.User(user_email=request.user_email, user_city=request.user_city,
                           user_name=request.user_name, password=hash_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@users_r.get("/{email}", response_model=user_model)
def index_(email, res: Response, db: session = Depends(get_db), current_user: User = Depends(token_lib.get_current_user)):
    users = db.query(models.User).filter(
        models.User.user_email == email).first()
    if(users == None):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usre not present")

    return users
