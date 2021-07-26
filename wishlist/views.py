import wishlist
from django.shortcuts import render, get_object_or_404, redirect
from .models import WishlistItem,Book, Wishlist

# Create your views here.

def addToWishlist(request, book_id):
    wishlist = get_object_or_404(Wishlist, user=request.user.id)
    book = get_object_or_404(Book,id=book_id)
    wish_list_item = WishlistItem.objects.create(wishlist=wishlist,book=book)    
    # return render(request, 'wishlist/wishlist.html', {'wish_list_item': wish_list_item})
    return redirect('wishlist:wishlistItems')

def wishlistItems(request):
    wishlist_items = WishlistItem.objects.all()
    return render(request, 'wishlist/wishlist.html', {'wishlist_items':wishlist_items})

def deleteFromWishlist(request, wishlistitem_id):
    item = get_object_or_404(WishlistItem, id=wishlistitem_id)
    item.delete()
    return redirect('wishlist:wishlistItems')

def clearwishlist(request):
    wishlist_items = WishlistItem.objects.all()
    clear = wishlist_items.delete()
    return redirect('books:bookStorePage')