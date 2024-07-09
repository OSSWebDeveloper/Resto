from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class Member(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.DateTimeField(max_length=100)
    country=models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True)