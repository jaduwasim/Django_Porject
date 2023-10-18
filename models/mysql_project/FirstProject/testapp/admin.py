from django.contrib import admin

# Register your models here.
from .models import Country, City

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ['id','name','country','population']