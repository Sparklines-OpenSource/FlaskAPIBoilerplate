from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy(engine_options={'max_identifier_length' : 128})

def initialize_db(app : Flask) -> None:
    db.init_app(app)