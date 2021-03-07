from . import main
from flask import render_template
from ..request import get_random_quote

@main.route('/', methods = ["GET", "POST"])
def index():
    return render_template('home.html')

@main.route('/quote')
def quote():
    '''
    Pulls/gets the random quotes
    '''

    title = "Quote || Dev Blog"
    quote = get_random_quote()
    return render_template('quote.html', title = title, quote = quote)