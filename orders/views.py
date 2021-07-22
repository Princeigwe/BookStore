from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem, Order

## this is a create order view.
"""when the form is filled, and validated, each item in the cart is created in the OrderItem model
and the cart is cleared"""

def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, bookName=item['book'],
                                quantity=item['quantity'],
                                unitPrice=item['price'],
                                totalPrice=item['total_price'])
            cart.clear()
            return redirect('payments:payment_process', id=order.id)
    
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'cart': cart, 'form':form})