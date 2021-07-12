from django.urls import path
from .views import homepage

urlpatterns = [
    path('', homepage, name='home'),
    path('<slug:genre_slug>/', homepage, name='homepage_with_category')
]