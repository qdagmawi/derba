from django.test import TestCase
from django.urls import reverse
from .models import Signup, Post

class CarAppTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = Signup.objects.create(
            first_name='Test',
            last_name='User',
            email='test@example.com',
            password='testpassword',
            phone_number='1234567890'
        )

        # Create some test cars
        self.car = Post.objects.create(
            user=self.user,
            model='Test Car',
            price=10000,
            car_make='Test Make',
            body_type='Sedan',
            transmission='Automatic',
            year='2022',
            color='Blue',
            description='This is a test car',
            phone_number='9876543210'
        )
