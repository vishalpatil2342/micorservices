from uuid import uuid4
import uvicorn 
from sqlmodel import Session,select
from fastapi import FastAPI,Depends,HTTPException,status,encoders
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT
from werkzeug.security import check_password_hash,generate_password_hash
from api.model import User
from api import schema
from api import database

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_headers=["*"],
  allow_methods=["*"]
)

def get_session():
  with Session(database.engine) as session:
    yield session

@AuthJWT.load_config
def get_config():
  return database.Settings()


@app.on_event('startup')
async def on_start():
  database.create_all()
  


@app.post('/signup',response_model=User,tags=['SIGNUP_USERS'])
async def signup(*,session:Session = Depends(get_session),user:schema.SignUpModel):
    db_username =  session.exec(select(User).where(User.username == user.username)).first()
    
    if db_username is not None:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User with these username exists")
    
    db_user_email = session.exec(select(User).where(User.email == user.email)).first()
    
    if db_user_email is not None:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User with these email exists")
    
    new_user = User(
      email=user.email,
      password=generate_password_hash(user.password),
      username=user.username,
      id=uuid4(),
    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    return new_user
  
  
  
@app.post('/login',tags=['LOGIN_USERS'])
async def login(*,session:Session = Depends(get_session),user:schema.LoginModel,Authorize:AuthJWT = Depends()):
  db_user_email = session.exec(select(User).where(User.email == user.email)).first()
    
  if db_user_email and check_password_hash(db_user_email.password,user.password):
    access_token = Authorize.create_access_token(subject=db_user_email.username)
    refresh_token = Authorize.create_refresh_token(subject=db_user_email.username)
    
    response = {
      "access":access_token,
      "refresh":refresh_token
    }
    return encoders.jsonable_encoder(response)
  raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid credentials")




@app.get('/refresh',tags=['GET_REFRESH_TOKEN'])
async def refresh_token(Authorize:AuthJWT = Depends()):
  try:
    Authorize.jwt_refresh_token_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="")

  current_user = Authorize.get_jwt_subject()
  
  access_token = Authorize.create_access_token(subject=current_user)
  
  return encoders.jsonable_encoder({"access":access_token})


@app.get('/user',tags=['GET_USER_BY_AUTENTICATION'])
async def get_user(Authorize:AuthJWT = Depends()):
  try:
    Authorize.jwt_required()
    
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

  current_user = Authorize.get_jwt_subject()
  return {"user":current_user}



@app.get('/users/{id}',tags=["GET_USER_BY_ID"])
def get_user(*,session:Session = Depends(get_session),id:str):
  user = session.get(User,id)
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
  return user



@app.get('/users',response_model=list[User],tags=['GET_ALL_USERS'])
def get_all_users(*,session:Session = Depends(get_session)):
  return session.exec(select(User)).all()

if __name__ == '__main__':
  uvicorn.run(host="localhost",port=8000,app=app)
