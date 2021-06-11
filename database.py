from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,session

SQLALCHEMY_DATABASE_URL = "postgres://stzaojmgcbyfjf:7bbb12c78fd5cb689bc8f71f3b264b6864575c62a917731519d72de0db038fe2@ec2-3-231-69-204.compute-1.amazonaws.com:5432/dfth4qdkruacod"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
