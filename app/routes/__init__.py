from flask import Blueprint
from .speed_routes import speed_bp

def register_blueprints(app):
    app.register_blueprint(speed_bp)