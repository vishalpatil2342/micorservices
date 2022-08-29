from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel,Field
from sqlalchemy import Column,String


class User(SQLModel,table=True): 
  id:Optional[UUID] = Field(default=uuid4(),primary_key=True)
  username:str = Field(sa_column=Column("username",String(55),unique=True))
  email:str = Field(sa_column=Column("email",String(55),unique=True))
  password:str 
  
  def __str__(self) -> str:
    return f"{self.username}"
  