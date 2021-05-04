from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from model import connect_to_db

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    connect_to_db(app)
    return app