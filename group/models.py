from django.db import models

# Create your models here.
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=32, default="null")

class ContactGroup(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.IntegerField()
    contact_id = models.IntegerField()

