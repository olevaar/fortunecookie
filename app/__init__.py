
from flask import Flask
from app.routes import message_routes

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(message_routes)

    return app
