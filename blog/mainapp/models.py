from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class UserBase(AbstractUser):
    login = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True)
    last_name = models.CharField(null=True, max_length=20)
    first_name = models.CharField(null=True, max_length=20)
    patronymic = models.CharField(null=True, max_length=20)
    date_create = models.DateTimeField(default=datetime.now)
    is_company = models.BooleanField(default=False)
    company = models.CharField(null=True, max_length=20, unique=True)
    about_me = models.CharField(null=True, max_length=500)
    logo = models.ImageField(null=True)