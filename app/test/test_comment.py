import unittest
from app.models import Comment, User
from app import db

class CommentTest(unittest.TestCase):
    '''
    Test Test Class to test the behaviour of the Comment class
    '''
    def setUp(self):
        self.user_John_Doe = User(username = 'John Doe', password = 'qwerty900', email = 'johndoe@gmail.com',
        profile_pi_path = 'https://image.tmdb.org/t/p/w500/jdjdjdjn', blog = 'talk is cheap show me the codes')
        self.new_comment = Comment(title = 'Lovely', comment = 'Thoughts on Atom? Anyone?', postedDate = '12,02,2021',
        user_id = 1234, pitch_id = 1234)

    def tearDown(self):
        Comment.Clear_comments()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.title, 'Lovely')
        self.assertEquals(self.new_comment.comment, 'Thoughts on Atom? Anyone?')
        self.assertEquals(self.new_comment.postedDate, '12,02,2021')
        self.assertEquals(self.new_review.user_id, 1234)
        self.assertEquals(self.new_review.pitch_id, 1234)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all() > 0))

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comment(1234)
        self.assertTrue(len(got_comments) == 1)