from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    user_photo = models.ImageField(upload_to='images/user_photos', null=True)
    about = models.CharField(max_length=300, blank=True)