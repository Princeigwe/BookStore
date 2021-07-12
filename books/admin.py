from django.contrib import admin
from .models import Genre,Book

# Register your models here.

admin.site.register(Genre)
admin.site.register(Book)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name')