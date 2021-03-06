from .models import Quote
import urllib.request, json

# Getting URL
quote_url = None

def configure_request(app):
    global quote_url
    quote_url = app.config['RANDOM_QUOTE_URL']

def get_random_quote():
    '''
    Function retrieves random quote and passing the JSON as the data intended
    '''
    with urllib.request.urlopen(quote_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)
        quote_results = None

        if quote_response['quote']:
            quote_items = quote_response['quote']
            quote_results = process_quote(quote_items)

    return quote_results

def process_quote(quote_list):
    '''
    Function Converts data to the class in the model
    '''
    quote = []
    for item in quote_list:
        author = item.get('author')
        quote_body = item.get('quote')
        new_quote = Quote(author, quote_body)
        quote.append(new_quote)

    return quote