from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourOwfour(error):
    '''
    Function to render the 404 error page
    '''
    title = '404 page'

    return render_template('404.html', title=title), 404
