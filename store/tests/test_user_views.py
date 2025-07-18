from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Book, Order, Lending

class UserHistoryTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.client.login(username='testuser', password='pass123')

    def test_empty_history(self):
        response = self.client.get('/user/history/')
        self.assertEqual(response.status_code, 200)
