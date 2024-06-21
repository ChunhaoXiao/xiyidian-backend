from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("mysql://root:123456@localhost/fastapi")
session = Session(engine)


def get_db():
    try:
        yield session
    finally:
        session.close()
        

