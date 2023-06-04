from django.db import models
from django.urls import reverse
# Create your models here.
class Beer(models.Model):
    name = models.CharField(max_length=128)
    taste = models.CharField(max_length=128)
    color = models.CharField(max_length=64)
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})