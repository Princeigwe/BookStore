from django.contrib import admin
from .models import Genre,Book

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class BookAdmin(admin.ModelAdmin):
    list_display = ['genre', 'title', 'author', 'price']
    
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
