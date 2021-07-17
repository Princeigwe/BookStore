from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from.models import Book, Genre
from django.contrib.auth.decorators import login_required
from cart.forms import QuantityForm

# Create your views here.

@login_required
def bookStorePage(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.all()
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = Book.objects.filter(genre=genre)
    return render(request,'books/book_list.html', { 'genre': genre, 'books': books, 'genres': genres })


@login_required
def bookDetail(request, pk):
    quantity_form = QuantityForm()
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book':book, 'quantity_form': quantity_form})