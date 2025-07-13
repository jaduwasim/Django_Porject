from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

phone_regex = RegexValidator(
    regex=r"^\d{10}", message="phone must be 10 Digit"
)

class StudentUser(AbstractUser):
    phone = models.CharField(unique=True, max_length=10, null=False, blank=False, validators=[phone_regex])
    image = models.ImageField(upload_to='media')