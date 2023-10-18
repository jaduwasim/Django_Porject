from django.contrib import admin
from .models import Page, Post, Song
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['user','Page_Name','Page_Cat','Page_Publish_Date']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','Post_Title','Post_Cat','Post_Publish_Date']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['Song_Name','Song_Duration', 'written_by']