from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class ExtendedUser(AbstractUser):
    date_of_birth = models.DateTimeField(auto_now_add=True)
