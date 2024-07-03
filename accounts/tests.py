from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Account

class AccountAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_account_with_negative_balance(self):
        url = '/accounts/'
        data = {
            "account_number": 12345,
            "account_name": "Savings Account",
            "account_type": "Savings",
            "balance": -500.00,
            "currency": "USD",
            "is_active": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('balance', response.data)  

    def test_create_account_with_positive_balance(self):
        url = '/accounts/'
        data = {
            "account_number": 12345,
            "account_name": "Savings Account",
            "account_type": "Savings",
            "balance": 1000.00,
            "currency": "USD",
            "is_active": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

