from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///taskmanager.db")

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass