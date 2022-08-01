from django.db import models


# Create your models here.
class UserDetails(models.Model):
    """
    create a class named as user details and given attributes
    """
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=20)
