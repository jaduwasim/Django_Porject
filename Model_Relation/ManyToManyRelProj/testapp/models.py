from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    user = models.ManyToManyField(User)
    Song_Name = models.CharField(max_length=70)
    Song_Duration = models.IntegerField()
    
    def written_by(self):
        return ", ".join([str(p) for p in self.user.all()])