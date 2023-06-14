from datetime import timedelta

class Config:
    DEBUG = True
    #Database related configs
    SQLALCHEMY_DATABASE_URI =  'sqlite:////data.sqlite'   
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #JWT Related configs
    JWT_SECRET_KEY = "secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    #OPENAPI Documentation configs
    APIFAIRY_TITLE = "Flask API"
    APIFAIRY_VERSION = "1.0.0"
    APIFAIRY_UI = "swagger_ui"

def initialize_app_config(app):
    app.config.from_object(Config)