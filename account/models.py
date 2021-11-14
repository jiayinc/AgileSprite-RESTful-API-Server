from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class ExtendedUser(AbstractUser):
    birthday = models.DateField(default="1901-01-01")
    # date_of_birth = '1970-01-01'
