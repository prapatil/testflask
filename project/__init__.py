#project/__init__.py
import os
from flask import Flask, jsonify
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
 app = Flask(__name__)
 # set config
 app_settings = os.getenv('APP_SETTINGS')
 app.config.from_object(app_settings)

 # set up extensions
 db.init_app(app)
 # register blueprints
 from project.api.views import users_blueprint
 app.register_blueprint(users_blueprint)

 return app

 
