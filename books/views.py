from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from.models import Book, Genre

# Create your views here.

def bookList(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.all()
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = Book.objects.filter(genre=genre)
    
    return render(request,'books/book_list.html', { 'genre': genre, 'books': books, 'genres': genres })
    
    