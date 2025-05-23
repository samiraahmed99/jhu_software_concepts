# blueprints setup
# has all the @bp.route() functions
from flask import Blueprint, render_template, url_for

bp = Blueprint('pages', __name__)

# use pages/ name of each page since they are in a 'pages' folder to separate my template html
@bp.route('/')
def home():
    return render_template('pages/home.html', page = 'home')

@bp.route('/contact')
def contact():
    return render_template('pages/contact.html', page = 'contact')

@bp.route('/projects')
def projects():
    return render_template('pages/projects.html', page = 'projects')

