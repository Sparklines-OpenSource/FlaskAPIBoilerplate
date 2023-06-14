from flask_cors import CORS
from flask import Flask

cors = CORS()

def initialize_cors(app : Flask) -> None:
    cors.init_app(app)