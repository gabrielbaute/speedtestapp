import logging
from flask import Flask
from database.db import session, engine
from database.models import Base
from logging.handlers import RotatingFileHandler

# Configuración del logger


def create_app():
    app=Flask(__name__)

    if not app.debug:
        file_handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=3)
        file_handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)

    with app.app_context():
        Base.metadata.create_all(engine)
    
    from app.routes import register_blueprints
    register_blueprints(app)

    return app