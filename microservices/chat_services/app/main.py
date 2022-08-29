import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event('startup')
def startup():
    pass



if __name__ == '__main__':
    uvicorn.run(app=app,host='localhost',port=8000)