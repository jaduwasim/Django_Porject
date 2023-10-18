from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Because of ForeignKey, One user can add Multiple Records
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Post_Title = models.CharField(max_length=70)
    Post_Cat = models.CharField(max_length=70)
    Post_Publish_Date = models.DateField()
