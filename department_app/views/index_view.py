'''
View for web application`s homepage

'''

from flask import Blueprint, render_template

index_bp = Blueprint('index_bp', __name__, template_folder='templates')


@index_bp.route("/")
@index_bp.route("/index")
def show_home():
    '''
    Function for show to user the homepage

    '''
    return render_template('index.html')
