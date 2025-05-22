# App factory function: creates and configures the app
from flask import Flask

# connect URL route "/" to the index() function by decorating it with @app.rout
@app.route('/')

def creat_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)

    return app



