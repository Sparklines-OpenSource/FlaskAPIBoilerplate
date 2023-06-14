from flask import Flask
from controllers.item_controller import item_bp


def initialize_blueprints(app : Flask) -> None:
    
    global_prefix = '/api'

    app.register_blueprint(item_bp, url_prefix=global_prefix+'/item')