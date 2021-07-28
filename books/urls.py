from django.urls import path
from .views import bookStorePage, bookDetail #, BookSearchResult

app_name='books'

urlpatterns = [
    path('books/', bookStorePage, name='bookStorePage'),
    path('<slug:genre_slug>/', bookStorePage, name='bookList_by_category'),
    path('book/<int:pk>/', bookDetail, name='book_detail' ),
    #path('write_review/<int:book_id>', writeReview, name='write_review'),
    #path('reviews/<int:book_id>/', bookReviews, name='book_reviews')
]