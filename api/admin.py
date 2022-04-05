from django.contrib import admin
from .models import User, Address, Geo, ToDo, Post, Comment, Album, Photo

# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Geo)
admin.site.register(ToDo)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(Photo)