from calendar import c
from sqlmodel import SQLModel,create_engine


engine = create_engine("sqlite:///../../../site.db",echo=True,connect_args={"check_same_thread":False})

def create_all():
    SQLModel.metadata.create_all(engine)