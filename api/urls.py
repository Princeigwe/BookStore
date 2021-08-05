from django.urls import path
from.views import GenreApiView, BookApiView, BookDetailApiView, UserListApiView, UserDetailApiView


urlpatterns = [
    path('genres/', GenreApiView.as_view()),
    path('books/', BookApiView.as_view()),
    path('book/<int:pk>/', BookDetailApiView.as_view()),
    path('users/', UserListApiView.as_view()),
    path('user/<int:pk>/', UserDetailApiView)
]