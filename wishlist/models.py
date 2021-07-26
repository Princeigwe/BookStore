from users.admin import CustomUser
from django.db import models
from django.contrib.auth import default_app_config, get_user_model
from books.models import Book
from django.conf import settings

# Create your models here.

CustomUser = get_user_model()

class Wishlist(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name="wishlistitem")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.book)