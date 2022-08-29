from uuid import UUID, uuid4
from sqlmodel import SQLModel,Field


class Posts(SQLModel):
    id:UUID = Field(primary_key=True,default=uuid4())
    