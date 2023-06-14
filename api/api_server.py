"""Welcome to My API Project!

## Project Overview

This is the project overview.

## Authentication

This is how authentication works.
"""

from flask import Flask
from configs.app_config import initialize_app_config
from configs.database import initialize_db, db
from configs.validator import initialize_validator
from configs.logger import intitalize_logger
from configs.cors import initialize_cors
from configs.jwt_manager import initialize_jwt_manager
from configs.app_docs import initialize_documentation
from .api_blueprints import initialize_blueprints

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    initialize_app_config(app)
    initialize_cors(app)
    initialize_db(app)
    initialize_validator(app)
    initialize_jwt_manager(app)
    intitalize_logger()
    initialize_documentation(app)
    initialize_blueprints(app)

    return app