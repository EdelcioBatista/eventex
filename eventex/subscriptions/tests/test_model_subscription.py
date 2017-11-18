from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Edelcio Batista',
            cpf='1234567890',
            email='edelcio.batista@gmail.com',
            phone='11-111111111'
        )
        self.obj.save()


    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have au auto created at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Edelcio Batista', str(self.obj))

