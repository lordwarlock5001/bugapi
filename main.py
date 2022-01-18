from sqlalchemy.orm import session
from schemas import User, user_model, Log_in
import models
from fastapi import FastAPI, Depends, Response, status, HTTPException,WebSocket
from typing import Optional, List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import engine, SessionLocal, get_db
from passlib.context import CryptContext
from routers import users,sockets
import token_lib
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(users.users_r)
app.include_router(sockets.sockets)
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.websocket("/textq")
async def test(websocket:WebSocket):
    await websocket.accept()
    data=None
    while True:
        data=await websocket.receive_text()
        if data!=None:
            await websocket.send_text("Hello "+str(data))
            data=None

@app.post("/login", tags=["Login"])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: session = Depends(get_db)):
    username = form_data.username
    password = form_data.password
    user = db.query(models.User).filter(
        models.User.user_email == username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid creadineals")

    if not user.email_verify:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"Error_code":42,"msg":"Email not verified"});
    if pwd_cxt.verify(password, user.password):
        return token_lib.create_access_token(data={"sub": username})
        return "login"
    else:
        raise HTTPException(
            status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail="Invalid creadineals")
    return token_lib.create_access_token(username)
