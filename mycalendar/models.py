from django.db import models

# Create your models here.


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, default="null")
    user_id = models.CharField(max_length=256, default="null")
    location = models.CharField(max_length=256, default="null")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    related_people = models.CharField(max_length=256, default="null")
    date = models.DateField()
    comments = models.TextField()
    category = models.CharField(max_length=256, default="null")
