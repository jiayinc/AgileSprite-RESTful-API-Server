from datetime import date

from django.db import models


# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=32, default="null")
    last_name = models.CharField(max_length=32, default="null")
    company = models.CharField(max_length=32, default="null")
    email = models.CharField(max_length=32, default="null")
    phone = models.CharField(max_length=32, default="null")
    mobile = models.CharField(max_length=32, default="null")
    address = models.CharField(max_length=512, default="null")
    birthday = models.DateField(default="1901-01-01")
    relationship = models.CharField(max_length=32, default="null")
    notes = models.CharField(max_length=256, default="null")
    image_address = models.CharField(max_length=256, default="null")
