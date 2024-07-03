from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from decimal import Decimal
from accounts.models import Account
from .models import Transfer

class AccountTransferTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.origin_account = Account.objects.create(
            account_number=111122223333,
            account_name='Sender Account',
            account_type='Checking',
            balance=Decimal('2000.00'),
            currency='USD'
        )
        self.destination_account = Account.objects.create(
            account_number=444455556666,
            account_name='Receiver Account',
            account_type='Savings',
            balance=Decimal('1000.00'),
            currency='USD'
        )

    def test_create_transfer(self):
        url = reverse('transfer-create')
        data = {
            'origin_account': self.origin_account.id,
            'destination_account': self.destination_account.id,
            'transfer_amount': '500.00',
            'transfer_type': 'Online',
            'transfer_code': 'TRN12345',
            'transfer_charge': '5.00',
            'status': 'Completed'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transfer.objects.count(), 1)

        self.origin_account.refresh_from_db()
        self.destination_account.refresh_from_db()

        self.assertEqual(self.origin_account.balance, Decimal('1500.00'))
        self.assertEqual(self.destination_account.balance, Decimal('1500.00'))

    def test_transfer_insufficient_funds(self):
        self.origin_account.balance = Decimal('100.00')
        self.origin_account.save()
        url = reverse('transfer-create')
        data = {
            'origin_account': self.origin_account.id,
            'destination_account': self.destination_account.id,
            'transfer_amount': '200.00',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transfer.objects.count(), 0)

        self.origin_account.refresh_from_db()
        self.destination_account.refresh_from_db()

        self.assertEqual(self.origin_account.balance, Decimal('100.00'))
        self.assertEqual(self.destination_account.balance, Decimal('1000.00'))

    def test_transfer_negative_amount(self):
        url = reverse('transfer-create')
        data = {
            'origin_account': self.origin_account.id,
            'destination_account': self.destination_account.id,
            'transfer_amount': '-100.00',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transfer.objects.count(), 0)

        self.origin_account.refresh_from_db()
        self.destination_account.refresh_from_db()

        self.assertEqual(self.origin_account.balance, Decimal('2000.00'))
        self.assertEqual(self.destination_account.balance, Decimal('1000.00'))

    def test_transfer_non_existent_account(self):
        non_existent_account_id = 99999
        url = reverse('transfer-create')
        data = {
            'origin_account': self.origin_account.id,
            'destination_account': non_existent_account_id,
            'transfer_amount': '100.00',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Transfer.objects.count(), 0)

        self.origin_account.refresh_from_db()
        self.destination_account.refresh_from_db()

        self.assertEqual(self.origin_account.balance, Decimal('2000.00'))
        self.assertEqual(self.destination_account.balance, Decimal('1000.00'))
