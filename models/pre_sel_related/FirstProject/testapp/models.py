from django.db import models

# Create your models here.
class Province(models.Model):   #Country
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'province'
    
class City(models.Model):
    name = models.CharField(max_length=60)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'city'

class Person(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    visitation = models.ManyToManyField(City, related_name='visitor')
    hometown = models.ForeignKey(City, on_delete=models.CASCADE, related_name='birth')
    living = models.ForeignKey(City, on_delete=models.CASCADE, related_name='citizen')

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'
    
    class Meta:
        db_table = 'person'

    def visitaion_city(self):
        return ', '.join([str(v) for v in self.visitation.all()])