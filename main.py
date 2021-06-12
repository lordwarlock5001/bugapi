from fastapi import FastAPI, Depends
from typing import Optional

app=FastAPI()
@app.get("/add")
def Create_U():
    return {"msg": "hello"}


@app.get("/")
def index_():
    return "welcome"
