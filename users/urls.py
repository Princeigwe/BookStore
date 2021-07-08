from django.urls import path
from .views import SignUpPageView

urlpatterns = [
    
    # no longer needed because of django-allauth
    # path('signup/', SignUpPageView.as_view(), name='signup')
]