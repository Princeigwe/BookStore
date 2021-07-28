from django.contrib import admin
from .models import Genre,Book, Review

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

class ReviewInline(admin.TabularInline):
    model = Review
    readonly_fields = ['reviewer', 'review', 'date_created']

    
class BookAdmin(admin.ModelAdmin):
    list_display = ['genre', 'title', 'author', 'price']
    inlines = [ReviewInline] 
    
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
