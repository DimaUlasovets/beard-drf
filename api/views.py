from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


from .models import User, ToDo, Post, Comment, Album, Photo

# Create your views here.
from .serializer import UserSerializer, ToDoSerializer, PostSerializer, CommentSerializer, AlbumSerializer, \
    PhotoSerializer


class UserCustomResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = Response(data)
        return response


class ToDoCustomResultsSetPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = Response(data)
        return response


class PostCustomResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = Response(data)
        return response


class CommentCustomResultsSetPagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = Response(data)
        return response


class AlbumCustomResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = Response(data)
        return response


class PhotoCustomResultsSetPagination(PageNumberPagination):
    page_size = 5000
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = Response(data)
        return response


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserCustomResultsSetPagination


class ToDoModelViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = ToDoCustomResultsSetPagination


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostCustomResultsSetPagination


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentCustomResultsSetPagination


class AlbumModelViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = AlbumCustomResultsSetPagination


class PhotoModelViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    pagination_class = PhotoCustomResultsSetPagination
