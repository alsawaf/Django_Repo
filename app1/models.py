from django.db import models

# Create your models here.

class user(models.Model):
    First_Name = models.CharField(max_length=32)
    Last_Name = models.CharField(max_length=32)
    Email = models.EmailField(max_length=124 , unique=True)
