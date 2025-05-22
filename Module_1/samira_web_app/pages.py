# blueprints setup
from flask import Blueprint, render_template

bp = Blueprint('pages', __name__, template_folder='templates')

# use pages/ name of each page since they are in a 'pages' folder to separate my template html
@bp.route('/')
def home():
    return render_template('pages/home.html')

@bp.route('/about')
def about():
    return render_template('pages/about.html')

@bp.route('/contact')
def contact():
    return render_template('pages/contact.html')

@bp.route('/projects')
def projects():
    return render_template('pages/projects.html')

