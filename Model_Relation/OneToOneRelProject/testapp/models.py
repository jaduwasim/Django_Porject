from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Because of OneToOneFeild, One user can add one one records
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
