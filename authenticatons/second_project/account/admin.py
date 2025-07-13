from django.contrib import admin
from account.models import UserModel
# Register your models here.


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display =  [
     "email" ,"phone" , "first_name","last_name" ,"is_active" ,"is_admin" ,"created_at" ,"updated_at" 
    ]
