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

    def __str__(self):
        return self.comment[:20]


class Message(models.Model):
    message = models.CharField(max_length=140, help_text='Max number of characters: 140', verbose_name='Your message')
    sent_by = models.ForeignKey(User, related_name='sent_by')
    sent_to = models.ForeignKey(User, related_name='sent_to')
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=True)

    def __str__(self):
        return self.message + ' - ' + self.sent_by.get_username()