from datetime import datetime

from django.shortcuts import resolve_url as r
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Adriano Leal',
            cpf='12345678901',
            email='adbrum@outlook.com',
            phone='966080448'
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Adriano Leal', str(self.obj))

    def test_paid_dafault_to_false(self):
        """By default paid must be false"""
        self.assertEqual(False, self.obj.paid)

    def test_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk, self.obj.key_hash)
        self.assertEqual(url, self.obj.get_absolute_url())