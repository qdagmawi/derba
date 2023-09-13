
from django.db import models


class Signup(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password_confirm = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    def name(self):
        return self.first_name

    objects = models.Manager()

