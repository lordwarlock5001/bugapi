from sqlalchemy.orm import session
from schemas import User, user_model, Log_in
import models

from fastapi import FastAPI, Depends, Response, status, HTTPException
from typing import Optional, List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import engine, SessionLocal
from passlib.context import CryptContext
import token_lib
print("main:packages")
models.Base.metadata.create_all(bind=engine)
print("main:files")
app = FastAPI()

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user", response_model=user_model)
def Create_U(request: User, db: session = Depends(get_db)):
    hash_pwd = pwd_cxt.hash(request.password)
    new_user = models.User(user_email=request.user_email, user_city=request.user_city,
                           user_name=request.user_name, password=hash_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/users", response_model=List[user_model])
def index_(db: session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.get("/user/{email}", response_model=user_model)
def index_(email, res: Response, db: session = Depends(get_db), current_user: User = Depends(token_lib.get_current_user)):
    users = db.query(models.User).filter(
        models.User.user_email == email).first()
    if(users == None):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usre not present")

    return users


@app.delete("/user/{email}")
def index_(email, res: Response, db: session = Depends(get_db)):
    try:
        db.query(models.User).filter(models.User.user_email ==
                                     email).delete(synchronize_session=False)
        db.commit()
    except Exception:
        HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usre not present")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/user/{email}")
def update(email, user_name, user_city, db: session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.user_email == email)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not present")
    db.query(models.User).filter(
        models.User.user_email == email).update({"user_name": user_name, "user_city": user_city}, synchronize_session=False)
    db.commit()

    return {"msg": "Updated"}

#form_data: OAuth2PasswordRequestForm = Depends()


@app.post("/user/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: session = Depends(get_db)):
    username = form_data.username
    password = form_data.password
    print(username)
    user = db.query(models.User).filter(
        models.User.user_email == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid creadineals")
    if pwd_cxt.verify(password, user.password):
        return token_lib.create_access_token(data={"sub": username})
        return "login"
    else:
        raise HTTPException(
            status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail="Invalid creadineals")
    return token_lib.create_access_token(username)
