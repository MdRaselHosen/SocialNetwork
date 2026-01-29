from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=15, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.email
