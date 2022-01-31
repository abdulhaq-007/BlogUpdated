from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    prepopulated_fields = {"slug":("name",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    prepopulated_fields = {"slug":("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','author','up', 'down', 'active']
	list_filter = ['up', 'author',"published"]
 
admin.site.register(Like)  
admin.site.register(Comment)  