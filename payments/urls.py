from django.urls import path
from .views import payment_process, payment_successful

app_name='payments'

urlpatterns = [
    path('<int:id>/', payment_process, name='payment_process'),
    # path('success/", PaymentSuccess.as_view(), name='payment_success' )
    path('success/<int:id>/', payment_successful, name='payment_successful' ),
]