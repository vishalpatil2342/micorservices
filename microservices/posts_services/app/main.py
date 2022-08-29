import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_orgins=["*"],
  allow_credentials=True,
  allow_headers=['*'],
  allow_methods=['*']
)




if __name__ == '__main__':
  uvicorn.run(app=app,host="localhost",port=8002)