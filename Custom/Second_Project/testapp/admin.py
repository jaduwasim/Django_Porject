from django.contrib import admin
from .models import CustomUser
# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','first_name','last_name','is_staff','phone', 'last_login']
# admin.site.register(CustomUser, UserAdmin)
