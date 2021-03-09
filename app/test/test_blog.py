
import unittest
from app.models import Blog, Comment, User


class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''
    def setUp(self):
        self.user_John_Doe = User(username = 'John Doe', password = 'qwerty900', email = 'johndoe@gmail.com',
        profile_pi_path = 'https://image.tmdb.org/t/p/w500/jdjdjdjn', blog = 'talk is cheap show me the codes')
        self.new_blog = Blog(blog_id = 1234, title = 'VS Code', body = 'We all love Visual Studio Code',
        postedDate = 'John Doe', user_id = 1234)

    def tearDown():
        Blog.Clear_blog()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_check_intasnce_variables(self):
        self.assertEquals(self.new_blog.blog_id, 1234)
        self.assertSetEquals(self.new_blog.blog_title, 'VS Code')
        self.assertSetEquals(self.new_blog.blog_body, 'We all love Visual Studio Code')
        self.assertSetEquals(self.new_blog.postedBy, 'John Doe')
        self.assertSetEquals(self.new_blog.user_id, 1234)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all() > 0))

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blogs = Blog.get_blogs(1234)
        self.asserTrue(len(got_blogs) == 1)