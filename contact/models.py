from datetime import date

from django.db import models


# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=32, default="null")
    email = models.CharField(max_length=32, default="null")
    birthday = models.DateField(default="1901-01-01")

