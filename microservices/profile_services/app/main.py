import uvicorn
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_orgins=["*"],
  allow_credentials=True,
  allow_headers=['*'],
  allow_methods=['*']
)

@app.get('/profile')
def get_profile():
  pass


@app.post('/profile')
def create_profile(req:Request):
  pass


if __name__ == '__main__':
  uvicorn.run(app=app,host='localhost',port=8001)
  