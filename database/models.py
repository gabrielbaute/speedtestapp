from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from .db import engine

Base=declarative_base()

class TestResults(Base):
    __tablename__="test_results"
    id=Column(Integer, primary_key=True)
    upload_speed=Column(Float, nullable=False)
    download_speed=Column(Float, nullable=False)
    latency=Column(Float, nullable=False)
    isp=Column(String)
    city=Column(String)
    country=Column(String)
    date_test=Column(DateTime, nullable=False)

class ErrorLog(Base):
    __tablename__="error_log"
    id=Column(Integer, primary_key=True)
    error_message=Column(String, nullable=False)
    date_occurred=Column(DateTime, nullable=False)

Base.metadata.create_all(engine)