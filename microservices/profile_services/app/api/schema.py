from pydantic import BaseModel


class ProfileInput(BaseModel):
    first_name:str
    last_name:str
    bio:str 
    education:str
    position:str
    country:str
    city:str
    user_id:str
    
    class Config:
        orm_mode = True
        
        
class ProfileOutput(BaseModel):
    id:str
    first_name:str
    last_name:str
    bio:str 
    education:str
    position:str
    country:str
    city:str
    user_id:str
    
    class Config:
        orm_mode = True