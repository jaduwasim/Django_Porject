from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=36)
    author = models.CharField(max_length=64)
    pages = models.IntegerField()
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})