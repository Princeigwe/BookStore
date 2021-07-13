from django.urls import path
from .views import bookStorePage

app_name='books'

urlpatterns = [
    path('books/', bookStorePage, name='bookStorePage'),
    path('books/<slug:genre_slug>/', bookStorePage, name='bookList_by_category' )
]