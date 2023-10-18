from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) #One to One Relation
    Page_Name = models.CharField(max_length=70)
    Page_Cat = models.CharField(max_length=70)
    Page_Publish_Date = models.DateField()

    class Meta:
        db_table = 'page'
    
    def __repr__(self) -> str:
        return f'{self.Page_Name}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #One to Many Relation
    Post_Title = models.CharField(max_length=70)
    Post_Cat = models.CharField(max_length=70)
    Post_Publish_Date = models.DateField()

    class Meta:
        db_table = 'post'
    
    def __repr__(self) -> str:
        return f'{self.Post_Title}'
    
class Song(models.Model):
    user = models.ManyToManyField(User) #Many to Many Relation 
    Song_Name = models.CharField(max_length=70)
    Song_Duration = models.IntegerField()

    class Meta:
        db_table = 'song'

    def __repr__(self) -> str:
        return f'{self.Song_Name}'
    
    def written_by(self):
        return ", ".join([str(p) for p in self.user.all()])