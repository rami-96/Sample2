from django.db import models


# Create your models here.
class Register(models.Model):
    FirstName = models.CharField(max_length=200)
    SurName = models.CharField(max_length=200)
    Email = models.EmailField(max_length=300)
    Password = models.TextField(max_length=300)
    DOB = models.DateField
    Gender = models.TextField



