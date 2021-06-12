from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,session

SQLALCHEMY_DATABASE_URL = "postgresql://uxlliftdzeeaxb:f9115df1505c5c3639700df62276028783cc80b4a3adb4c096f791b8413c4f88@ec2-34-193-112-164.compute-1.amazonaws.com:5432/dfbuo5b2rlhnnp"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
