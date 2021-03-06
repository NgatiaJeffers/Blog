from . import main
from flask import render_template
from ..request import get_random_quote

@main.route('/')
def index():
    return render_template('home.html')