from django.urls import path
from .views import homepage

app_name = 'pages'

urlpatterns = [
    path('home/', homepage, name='home'),
    path('home/<slug:genre_slug>/', homepage, name='homepage_with_category')
]