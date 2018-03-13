from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)


class Comments(models.Model):
    comment = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    tweet = models.ForeignKey(Tweet)

