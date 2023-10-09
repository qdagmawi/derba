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

    def test_post_car(self):
        # Log in the user first
        self.client.login(email='test@example.com', password='testpassword')

        response = self.client.post(reverse('car:post_car'), {
            'model': 'New Car',
            'price': 15000,
            'car_make': 'New Make',
            'body_type': 'SUV',
            'transmission': 'Manual',
            'year': '2023',
            'color': 'Red',
            'description': 'This is a new test car',
            'phone_number': '1231231234'
        })

        self.assertEqual(response.status_code, 302)

    def test_user_logout(self):
        response = self.client.get(reverse('car:user_logout'))
        self.assertEqual(response.status_code, 302)

    def test_invalid_login(self):
        response = self.client.post(reverse('car:log'), {'email': 'nonexistent@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid credentials')

    def test_valid_login(self):
        response = self.client.post(reverse('car:log'), {'email': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)

  
    def test_signup_view(self):
        response = self.client.get(reverse('car:signup'))
        self.assertEqual(response.status_code, 200)


    def test_index_view(self):
        response = self.client.get(reverse('car:index'))
        self.assertEqual(response.status_code, 200)

    def test_post_car_view(self):
        # Log in the user first
        self.client.login(email='test@example.com', password='testpassword')

        response = self.client.get(reverse('car:post_car'))
        self.assertEqual(response.status_code, 200)


    def test_login_view(self):
        response = self.client.get(reverse('car:login'))
        self.assertEqual(response.status_code, 200)
