from django.contrib import admin
from account.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','profile_img']