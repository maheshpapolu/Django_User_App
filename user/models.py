from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserDetails(AbstractUser):
    """
    create a class named as user details and given attributes
    """
    # username = models.CharField(max_length=200)
    # password = models.CharField(max_length=20)
    # email = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
