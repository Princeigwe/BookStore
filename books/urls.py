from django.urls import path
from .views import bookList

urlpatterns = [
    path('', bookList, name='book_list')
]