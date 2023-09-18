
from django.db import models


class Signup(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password_confirm = models.CharField(max_length=100)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name

    def name(self):
        return self.first_name

    objects = models.Manager()


class Post(models.Model):
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    car_make = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.model

    objects = models.Manager()

