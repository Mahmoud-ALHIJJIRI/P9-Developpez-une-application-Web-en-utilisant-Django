from django.db import models
from django.core.validators import MinLengthValidator


"""class User(models.Model):
    first_name = models.fields.CharField(max_length=30)
    last_name = models.fields.CharField(max_length=30)
    age = models.fields.IntegerField()
    email_address = models.fields.CharField(max_length=30)
    password = models.fields.CharField(validators=[MinLengthValidator(8)])
    password1 = models.fields.CharField(validators=[MinLengthValidator(8)])
    def __str__(self):
        return self.first_name"""
