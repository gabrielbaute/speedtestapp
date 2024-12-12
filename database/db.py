from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine=create_engine("sqlite:///tests.db")
Session=sessionmaker(bind=engine)
session=Session()

def save_test_result(upload_speed, download_speed, latency, isp, city, country, date_test):
    from .models import TestResults
    new_result=TestResults(
        upload_speed=upload_speed,
        download_speed=download_speed,
        latency=latency,
        isp=isp,
        city=city,
        country=country,
        date_test=date_test
    )
    session.add(new_result)
    session.commit()

def log_error(error_message):
    from .models import ErrorLog
    new_error=ErrorLog(
        error_message=error_message,
        date_occurred=datetime.now()
    )
    session.add(new_error)
    session.commit()
