from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    phone = models.IntegerField(verbose_name='Mobile No', unique=True)

    REQUIRED_FIELDS = ['first_name','last_name','phone','email']

    def __str__(self) -> str:
        return f"Phone:{self.phone} F_Name:{self.first_name} L_Name{self.last_name} "
    class Meta:
        db_table = 'User'