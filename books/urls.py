from django.urls import path
from .views import bookStorePage

app_name='books'

urlpatterns = [
    path('', bookStorePage, name='bookStorePage'),
    path('<slug:genre_slug', bookStorePage, name='bookList_by_category' )
]