from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class UserLogin(BaseModel):
    username:str
    password:str

class UserRegister(BaseModel):
    username:str
    password:str
    email:str

@router.post("/login")
def login(request:UserLogin):
    return {"message": "User logged in successfully"}

@router.post("/register")
def register(request:UserRegister):
    return {"message": "User registered successfully"}