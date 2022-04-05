from django.test import TestCase
from .models import User, Address, Geo, ToDo, Post, Comment, Album, Photo


# Create your tests here.

class ModelTesting(TestCase):

    def setUp(self):
        self.geo = Geo.objects.create(
            lat='-12.123', lng='21.2131'
        )
        self.addr = Address.objects.create(
            street='Tanka', suite='12',
            city='Minsk', zipcode='220004',
            geo=self.geo
        )
        self.user = User.objects.create(
            name='Dima Ulasovets', username='d.ulasovets',
            email='test@mail.ru', address=self.addr
        )
        self.todo = ToDo.objects.create(
            userId=self.user, title='Test title', completed='true'
        )
        self.post = Post.objects.create(
            userId=self.user, title='Test Post', body='Some text'
        )
        self.comment = Comment.objects.create(
            postId=self.post, name='Test comment',
            email='test@mail.ru', body='some text'
        )
        self.album = Album.objects.create(
            userId=self.user, title='Cool Album'
        )
        self.photo = Photo.objects.create(
            albumId=self.album, title='Cool dog',
            url='https://qweweqewq.com', beard='http://beard/12312.com')

    def test_user_model(self):
        data = self.user
        self.assertTrue(isinstance(data, User))
        self.assertEqual(str(data), 'Dima Ulasovets')

    def test_todo_model(self):
        data = self.todo
        self.assertTrue(isinstance(data, ToDo))
        self.assertEqual(str(data), 'Test title')

    def test_post_model(self):
        data = self.post
        self.assertTrue(isinstance(data, Post))
        self.assertEqual(str(data), 'Test Post')

    def test_address_model(self):
        data = self.addr
        self.assertTrue(isinstance(data, Address))
        self.assertEqual(str(data), 'Tanka')

    def test_comment_model(self):
        data = self.comment
        self.assertTrue(isinstance(data, Comment))
        self.assertEqual(str(data), 'Test comment')

    def test_album_model(self):
        data = self.album
        self.assertTrue(isinstance(data, Album))
        self.assertEqual(str(data), 'Cool Album')

    def test_photo_model(self):
        data = self.photo
        self.assertTrue(isinstance(data, Photo))
        self.assertEqual(str(data), 'Cool dog')
