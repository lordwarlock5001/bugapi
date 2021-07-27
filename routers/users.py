from fastapi import APIRouter, Depends, Response, status, HTTPException,BackgroundTasks
from schemas import User, user_model, Log_in
from hashing import create_hash, verify_hash
import models
from database import get_db, session
import token_lib
import random
from send_email import send_email_background,send_email_async
from datetime import datetime,timedelta
users_r = APIRouter(
    prefix="/user",
    tags=["User"]
)


    

@users_r.post("/", response_model=user_model)
def Create_U(request: User, db: session = Depends(get_db)):
    hash_pwd = create_hash(request.password)
    new_user = models.User(user_email=request.user_email, user_city=request.user_city,
                           user_name=request.user_name, password=hash_pwd,email_verify=False,otp_time=None)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@users_r.post("/verify_req")
async def verify_req(email:str,db: session = Depends(get_db)):
    users = db.query(models.User).filter(
        models.User.user_email == email).first()
    if(users == None):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not present")
    
    otp=random.randint(100000,999999)
    up=db.query(models.User).filter(
        models.User.user_email == email).update({"otp_time":datetime.now(),"otp":otp})    
    db.commit()
    await send_email_async(subject="Verify your email",email_to=email,body_e={"Title":"Verify Your OTP","otp":str(otp),"name":users.user_name})
    return "Otp send successfully"

@users_r.post("/verify_otp")
def verify_otp(email:str,otp:int ,db: session = Depends(get_db)):
    users = db.query(models.User).filter(
        models.User.user_email == email).first()
    if(users == None):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not present")
    if(users.otp_time == None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not verified")
    if(datetime.now()-users.otp_time > timedelta(minutes=5)):
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Otp is experired")
    if(users.otp == None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Otp not present")
    if(users.otp == int(otp)):
        users.email_verify = True
        db.commit()
        return "Verified"
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Otp is invalid")
    
@users_r.get("/", response_model=user_model)
def index_(email:str, res: Response, db: session = Depends(get_db), current_user: User = Depends(token_lib.get_current_user)):
    users = db.query(models.User).filter(
        models.User.user_email == email).first()
    if(users == None):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not present")

    return users
