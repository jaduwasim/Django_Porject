from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name='First Name', max_length=255,)
    last_name = models.CharField(verbose_name='Last Name', max_length=255)
    phone = models.IntegerField(verbose_name='Mobile No')

    REQUIRED_FIELDS = ['email','phone', 'first_name','last_name']

    class Meta:
        db_table = 'User'

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper().strip()
        self.last_name = self.last_name.capitalize().strip()
        self.email = self.email.strip()
        super().save(*args, **kwargs)