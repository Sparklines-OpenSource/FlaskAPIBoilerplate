from apifairy import APIFairy
from flask import Flask

docs = APIFairy()


def initialize_documentation(app : Flask):
    docs.init_app(app)