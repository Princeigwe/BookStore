from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from.models import Book, CustomUser, Genre, Review
from django.contrib.auth.decorators import login_required
from cart.forms import QuantityForm
from .forms import ReviewForm
from django.contrib.auth import get_user_model


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
    """the book detail view function has the same
    functionalities of adding book to cart, writing reviews and viewing review of the particular book"""
    quantity_form = QuantityForm()
    book = get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.reviewer = request.user
            review.save()

    else:
        form = ReviewForm()
    return render(request, 'books/book_detail.html', {'book':book, 'quantity_form': quantity_form, 'reviews': reviews, 'form':form})



# @login_required
# def writeReview(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.book = book
#             review.reviewer = request.user
#             review.save()

#     else:
#         form = ReviewForm()
#     return render(request, 'books/book_detail.html', {'form':form, 'book':book})

# @login_required
# def bookReviews(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     reviews = Review.objects.filter(book=book)
#     return render(request, 'books/book_detail.html', {'reviews': reviews, 'book':book})