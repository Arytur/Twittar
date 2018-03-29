from django.test import TestCase

from twittar_app.models import *


class TweetModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified object used by all test method
        user = User.objects.create(username='testuser', password='12345')
        Tweet.objects.create(content='Some example content to display', user=user)

    def test_content_label(self):
        tweet = Tweet.objects.get(id=1)
        field_label = tweet._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'Your message')

    def test_content_max_length(self):
        tweet = Tweet.objects.get(id=1)
        max_length = tweet._meta.get_field('content').max_length
        self.assertEquals(max_length, 140)

    def test_tweet_display_twenty_letters_of_content(self):
        tweet = Tweet.objects.get(id=1)
        self.assertEquals(20, len(str(tweet)))

