from rest_framework.serializers import ModelSerializer

from .models import User, ToDo, Post, Comment, Album, Photo


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'address']
        depth = 2


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['userId', 'id', 'title', 'completed']
        # depth = 2


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['userId', 'id', 'title', 'body']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['postId', 'id', 'name', 'email', 'body']


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ['userId', 'id', 'title']


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['albumId', 'id', 'title', 'url', 'beard']
