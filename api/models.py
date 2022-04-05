from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, blank=True, null=False)
    username = models.CharField(max_length=20, blank=True, null=False)
    email = models.CharField(max_length=30, blank=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=50, blank=True, null=False)
    suite = models.CharField(max_length=50, blank=True, null=False)
    city = models.CharField(max_length=50, blank=True, null=False)
    zipcode = models.IntegerField(blank=True, null=True)
    geo = models.ForeignKey('Geo', on_delete=models.CASCADE)

    def __str__(self):
        return self.street


class Geo(models.Model):
    lat = models.CharField(max_length=50, blank=True, null=False)
    lng = models.CharField(max_length=50, blank=True, null=False)


class ToDo(models.Model):

    complete_res = (
        ('False', 'false'),
        ('True', 'true')
    )

    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=False)
    completed = models.CharField(choices=complete_res, max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=False)
    body = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.CharField(max_length=50, blank=True, null=False)
    body = models.CharField(max_length=300, blank=True, null=False)

    def __str__(self):
        return self.name


class Album(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):
        return self.title


class Photo(models.Model):
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=False)
    url = models.CharField(max_length=200, blank=True, null=False)
    beard = models.CharField(max_length=200, blank=True, null=False)

    def __str__(self):
        return self.title