from . import main
from flask import render_template
from ..requests import get_random_quote
from ..models import Blog, Comment
from flask_login import current_user, login_required

@main.route('/')
def index():
    quotes = get_random_quote()
    blog = Blog.query.all()
    return render_template('index.html', quotes = quotes, blog = blog, user = current_user)

