from django.db import models


# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    birth_date = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
