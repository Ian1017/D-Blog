from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    View root page  function that return index and its data
    '''
    title = "Ian's Blog"
    intro = "Welcome to my journey"

    return render_template('index.html, title = title, intro = intro')