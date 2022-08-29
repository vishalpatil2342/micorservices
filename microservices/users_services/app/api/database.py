import os
from sqlmodel import SQLModel,create_engine
from pydantic import BaseModel

class Settings(BaseModel):
  authjwt_secret_key:str = 'vishal_patil'



engine = create_engine("sqlite:///../../../site.db",echo=True,connect_args={"check_same_thread":False})
  
def create_all():
  SQLModel.metadata.create_all(bind=engine)