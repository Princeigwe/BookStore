from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from .forms import QuantityForm
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import QuantityForm

# Create your views here.

def cart_detail(request):
    cart = Cart(request)
    
    for item in cart:
        item['update_quantity_form'] = QuantityForm(initial={ 'quantity': item['quantity'], 'override': True })
    return render(request, 'cart/cart_detail.html', {'cart': cart, })

# function to adding book to the cart
@require_POST
def cart_add(request, book_id):
    form = QuantityForm(request.POST)
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    
    if form.is_valid():
        cd = form.cleaned_data ## getting the input values from the form, and adding it to the cart
        cart.addBook(book=book, quantity=cd['quantity'], override_quantity=cd['override'])
        return redirect('cart:cart_detail')



def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    
    cart.removeBook(book)
    return redirect('cart:cart_detail')
