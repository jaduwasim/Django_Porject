from django.contrib import admin
from .models import Country, City
# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id','name','country','population']

