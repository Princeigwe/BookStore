from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from books.models import Book, Genre
import random

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def homepage(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.filter(price__range=(500.00, 700.00))
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = Book.objects.filter(genre=genre, price__range=(500.00, 700.00))
    
    return render(request,'home.html', { 'genre': genre, 'books': books, 'genres': genres })
    
    