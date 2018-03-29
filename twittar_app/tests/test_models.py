from django.test import TestCase

from twittar_app.models import *


class TweetModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified object used by all test method
        user = User.objects.create(username='testuser', password='12345')
        Tweet.objects.create(content='Some example content to display', user=user)

    def test_content_label(self):
        tweet = Tweet.objects.get(id=2)
        field_label = tweet._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'Your message')

    def test_content_max_length(self):
        tweet = Tweet.objects.get(id=2)
        max_length = tweet._meta.get_field('content').max_length
        self.assertEquals(max_length, 140)

    def test_tweet_display_twenty_letters_of_content(self):
        tweet = Tweet.objects.get(id=2)
        self.assertEquals(20, len(str(tweet)))


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified object used by all test method
        user = User.objects.create(username='testuser', password='12345')
        tweet = Tweet.objects.create(content='Some example content to display', user=user)
        Comments.objects.create(comment='Some example comment to display', user=user, tweet=tweet)

    def test_comment_label(self):
        comment = Comments.objects.get(id=1)
        field_label = comment._meta.get_field('comment').verbose_name
        self.assertEquals(field_label, 'Your message')

    def test_comment_max_length(self):
        comment = Comments.objects.get(id=1)
        max_length = comment._meta.get_field('comment').max_length
        self.assertEquals(max_length, 140)

    def test_tweet_display_twenty_letters_of_content(self):
        comment = Comments.objects.get(id=1)
        self.assertEquals(20, len(str(comment)))


class MessageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username='userone', password='234566')
        user2 = User.objects.create(username='usertwo', password='345678')
        message = Message.objects.create(message='Some example message to send', sent_by=user1, sent_to=user2)

    def test_message_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('message').verbose_name
        self.assertEquals(field_label, 'Your message')

    def test_message_max_length(self):
        message = Message.objects.get(id=1)
        max_length = message._meta.get_field('message').max_length
        self.assertEquals(max_length, 140)
