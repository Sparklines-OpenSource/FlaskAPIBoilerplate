from flask_marshmallow import Marshmallow
from flask import Flask

validator = Marshmallow()

def initialize_validator(app : Flask) -> None:
    validator.init_app(app)