from app.models import Comment,User
from app import db

def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_comment = Comment(movie_id=12345,movie_title='Comment for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_comment='This movie is the best thing since sliced bread',user = self.user_James )

def tearDown(self):
        Comment.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.movie_id,12345)
        self.assertEquals(self.new_comment.movie_title,'Comment for movies')
        self.assertEquals(self.new_comment.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_comment.movie_comment,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_comment.user,self.user_James)

def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

def test_get_review_by_id(self):

        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)
