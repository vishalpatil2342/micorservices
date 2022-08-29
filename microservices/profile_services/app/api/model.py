from typing import Optional
from sqlmodel import SQLModel,Field


class Profile(SQLModel,table=True):
    id:str = Field(primary_key=True)
    first_name:str
    last_name:str
    bio:str 
    education:str
    position:str
    country:str
    city:str
    user_id:Optional[str] = Field(default=None,foreign_key='user.id')