from pydantic import BaseModel,EmailStr

class SignUpModel(BaseModel):
  username:str
  email:EmailStr
  password:str
  
  class Config:
    orm_mode:True
  
class LoginModel(BaseModel):
  email:EmailStr
  password:str
  
  class Config:
    orm_mode:True