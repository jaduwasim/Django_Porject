from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status'] #Here we have to specify the field names which have to display
    list_filter = ('status', 'title','author', 'created' ,'publish',) #To filter records based on our provided fields (As the result, on the Right hand side side bar will be appeared for filtering purpose)
    search_fields = ['title'] #A search bar appeared on the page
    prepopulated_fields = {'slug':('title',)} #If we type title then the same value will be considered automatically for the slug field also
    raw_id_fields = ('author',) #author field is displayed with lookup widget,that can scale better than dropdown list. This is helpful if huge number of values are available.
    date_hierarchy = 'publish' #Below search button,we can see a bar to navigate quickly based on published date.
    ordering = ['status','publish'] #To display records according to specified order


admin.site.register(Post, PostAdmin)