from fastapi import FastAPI,Depends
from typing import Optional
from database import engine,SessionLocal
import models
from schemas import User
from sqlalchemy.orm import session
models.Base.metadata.create_all(bind=engine)

app=FastAPI()
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

@app.post("/add")
def Create_U(request:User,db:session=Depends(get_db)):
    new_user=models.User(user_email=request.user_email,user_city=request.user_city,user_name=request.user_name,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user