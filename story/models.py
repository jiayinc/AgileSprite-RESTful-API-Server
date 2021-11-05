from django.db import models


# Create your models here.
class Story(models.Model):
    id = models.AutoField(primary_key=True)
    contact_id = models.IntegerField()
    user_id = models.IntegerField()
    location = models.CharField(max_length=256, default="null")
    date = models.DateField(default="1901-01-01")
    content = models.CharField(max_length=256, default="null")
