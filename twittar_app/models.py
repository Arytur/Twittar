from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=140, help_text='Max number of characters: 140', verbose_name='Your message')
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.content[:20]


class Comments(models.Model):
    comment = models.CharField(max_length=140, help_text='Max number of characters: 140', verbose_name='Your message')
    user = models.ForeignKey(User)
    tweet = models.ForeignKey(Tweet)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.comment[:20]

