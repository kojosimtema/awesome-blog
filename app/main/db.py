from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///blogdatabase.db")

session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

# Base.metadata.create_all(bind=engine)