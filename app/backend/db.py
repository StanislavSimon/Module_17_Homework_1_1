from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from slugify import slugify
engine = create_engine("sqlite:///taskmanager.db", echo=True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


