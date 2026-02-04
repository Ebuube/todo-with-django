from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthFlowTests(TestCase):
    def test_signup_logs_user_in_and_redirects(self):
        url = reverse('core:signup')
        resp = self.client.post(url, data={
            'username': 'amaka',
            'email': 'amaka@example.com',
            'password1': 'StrongPassword!234',
            'password2': 'StrongPassword!234',
        })
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(User.objects.filter(username='amaka').exists())

        # Should be logged in
        dashboard = self.client.get(reverse('todos:dashboard'))
        self.assertEqual(dashboard.status_code, 200)

    def test_login_works(self):
        User.objects.create_user(
            username='u1',
            email='u1@example.com',
            password='StrongPassword!234'
        )
        resp = self.client.post(reverse('core:login'), data={
            'username': 'u1',
            'password': 'StrongPassword!234',
        })
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(self.client.get(reverse('todos:dashboard')).status_code, 200)
