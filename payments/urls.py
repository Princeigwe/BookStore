from django.urls import path
from .views import payment_process

app_name='payments'

urlpatterns = [
    path('<int:id>/', payment_process, name='payment_process')
]