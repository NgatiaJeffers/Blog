from . import main
from flask import render_template
from ..requests import get_random_quote
from ..models import Blog, Comment

@main.route('/')
def index():
    quotes = get_random_quote()

    return render_template('index.html', quotes = quotes)