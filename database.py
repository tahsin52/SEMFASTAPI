from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:postgres@localhost:5432/sem', echo=True)
# echo=True is for debugging purpose

Base = declarative_base()

Session = sessionmaker(bind=engine)