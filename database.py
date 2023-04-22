from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://rsxcfqrakemmmn:325a543023e7b16c2612f589ac12b7cc1eca321b2ef35a70704b1e2f7c8cba36@ec2-3-234-204-26.compute-1.amazonaws.com:5432/dbqjq6upc6c96l"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()