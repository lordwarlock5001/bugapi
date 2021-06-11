from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,session

SQLALCHEMY_DATABASE_URL = "postgres://cyrvcmwerwegek:b96dd8be6079e019632c13464a7e483645a2bedf5d191536b35f4c5e66d08366@ec2-54-211-55-24.compute-1.amazonaws.com:5432/d5vg3bqvsednid"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
