from django.contrib import admin

# Register your models here.
from .models import Person, City, Province

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('id','name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'province')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','visitaion_city','hometown','living')