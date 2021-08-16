from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order
from django.conf import settings
from django.views.generic import TemplateView

# Create your views here.

# class PaymentSuccess(TemplateView):
#     template_name = "payments/payment_success.html"
    


def payment_process(request, id):
    
    order = get_object_or_404(Order, id=id)
    total_cost = order.totalPrice()
    
    #publicKey = settings.RAVE_LIVE_PUBLIC_KEY
    publicKey = settings.RAVE_LIVE_PUBLIC_KEY
    amount = total_cost
    customer_email = order.email
    customer_Name = order.customer_firstname + order.customer_lastname
    tx_ref = "bKSt9302" + str(order.id)
    return render(
        request,
        'payments/payment_page.html',
        {'publicKey': publicKey,
        'amount': amount,
        'customer_email': customer_email,
        'customerName': customer_Name,
        'tx_ref':tx_ref,
        'id':order.id,}
    )


"""this dunction gets the current id from the http request, in order to mark paid as true"""
def payment_successful(request, id):
    
    #id = payment_process(request,id=id)
    order = get_object_or_404(Order, id=id)
    order.paid = True
    order.save()
    return render(request, "payments/payment_success.html", {'id':id})


# function for unsuccessful payment
def payment_unsuccessful(request):
    return render(request, "payments/payment_failed.html")