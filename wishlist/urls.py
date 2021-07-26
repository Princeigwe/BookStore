from django.urls import path
from .views import addToWishlist, wishlistItems, deleteFromWishlist, clearwishlist

app_name='wishlist'

urlpatterns = [
    path('add/<int:book_id>/wishlist', addToWishlist, name="add_wishlistitem"),
    path('items/', wishlistItems, name="wishlistItems"),
    path('delete/item<int:wishlistitem_id>/wishlist', deleteFromWishlist, name="delete_wishlistitem"),
    path('clear/', clearwishlist, name="clearwishlist")
]