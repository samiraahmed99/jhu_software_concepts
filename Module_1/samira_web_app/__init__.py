# App factory function: creates and configures the app
from flask import Flask

# Import pages module where the Blueprint is defined in current working directory ( i.e.`.`)
from samira_web_app import pages


def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)  # Register the Blueprint from pages.py
    return app