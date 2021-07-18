from django.urls import path
from .views import cart_add, cart_remove, cart_detail

app_name='cart'

urlpatterns = [
    path('detail/', cart_detail, name='cart_detail' ), 
    path('add-book/<int:book_id>/', cart_add, name='cart_add'),
    path('remove-book/<int:book_id>/', cart_remove, name='cart_remove')
]