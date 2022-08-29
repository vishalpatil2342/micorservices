from sqlmodel import SQLModel,create_engine


engine = create_engine('sqlite:///../../../sqlite.db')


def create_table():
    SQLModel.metadata.create_all(engine)