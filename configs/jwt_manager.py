from flask_jwt_extended import JWTManager
from flask import Flask

jwt = JWTManager()

def initialize_jwt_manager(app : Flask) -> None:
    jwt.init_app(app)