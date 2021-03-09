import unittest
from app.models import Quote 

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that wil run before every Test
        '''
        self.new_quote = Quote(1234, 'John Doe', 'A thrilling new Python Series')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Quote))