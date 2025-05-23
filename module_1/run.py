from flask import Flask

# import creat_app() function from __init__.py located in our web application module
from samira_web_app import create_app
# create a Flask application instance
app = create_app()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)
