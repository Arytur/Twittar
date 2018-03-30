from django.test import TestCase

from django.urls import reverse
from django.contrib.auth.models import User


class MainPageViewTest(TestCase):

    def setUp(self):
        # create a user
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser', password='12345')
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('main'))
        self.assertEqual(resp.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('main'))
        self.assertRedirects(resp, '/accounts/login/?next=/')

    def test_logged_in_uses_correct_templates(self):
        login = self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('main'))

        # Check if user is logged in
        self.assertEqual(str(resp.context['user']), 'testuser')
        # Check the response "success"
        self.assertEqual(resp.status_code, 200)

        # Check the use correct template
        self.assertTemplateUsed(resp, 'main.html', 'base.html')
