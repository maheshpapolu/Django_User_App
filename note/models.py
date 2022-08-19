from django.db import models
from user.models import UserDetails


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
