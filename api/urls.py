from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'users', views.UserModelViewSet)
router.register(r'todos', views.ToDoModelViewSet)
router.register(r'posts', views.PostModelViewSet)
router.register(r'comments', views.CommentModelViewSet)
router.register(r'albums', views.AlbumModelViewSet)
router.register(r'photos', views.PhotoModelViewSet)

urlpatterns = [
                  path('api/', include(router.urls)),
              ] + router.urls
