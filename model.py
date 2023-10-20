from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Directory(Base):
    __tablename__ = 'directories'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    emails = Column(ARRAY(String), nullable=True)