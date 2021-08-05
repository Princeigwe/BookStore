from django.shortcuts import render
from rest_framework import generics
from books.models import CustomUser, Genre, Book
from django.contrib.auth import get_user_model
from .serializers import GenreSerializer, BookSerializer, UserSerializer


# Create your views here.

CustomUser = get_user_model()

class GenreApiView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserListApiView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetailApiView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer