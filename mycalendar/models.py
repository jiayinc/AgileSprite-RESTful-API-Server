from django.db import models

# Create your models here.


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, default="null")
    user_id = models.CharField(max_length=256, default="null")
    location = models.CharField(max_length=256, default="null")
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    related_people = models.CharField(max_length=256, default="null")
    comments = models.TextField()
    category = models.CharField(max_length=256, default="null")
