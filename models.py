from django.db import models
from django_cryptography.fields import encrypt

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = encrypt(models.CharField(max_length=15))
    aadhaar_number = encrypt(models.CharField(max_length=12))

    def __str__(self):
        return self.name
