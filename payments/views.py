from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order
from django.conf import settings
from django.views.generic import TemplateView

# Create your views here.

# class PaymentPage(TemplateView):
#     template_name = 'payments/payment_page.html'
    
#     def get_context_data(self, request, **kwargs):
#         context = super().get_context_data(**kwargs)
#         order_id = request.session.get('order_id')
#         order = get_object_or_404(Order, id=order_id)
#         total_cost = order.totalPrice()
#         tx_ref = "bKSt9302" + str(order.id)
        
#         context['publicKey'] = settings.RAVE_PUBLIC_KEY
#         context['amount'] = total_cost
#         context['customer_email'] = order.email
#         context['tx-ref'] = tx_ref
#         context['telephone'] = order.telephone
#         return context


class PaymentSuccess(TemplateView):
    template_name = "home.html"



def payment_process(request, id):
    
    order = get_object_or_404(Order, id=id)
    total_cost = order.totalPrice()
    
    publicKey = settings.RAVE_PUBLIC_KEY
    amount = total_cost
    customer_email = order.email
    customer_Name = order.customer_firstname + order.customer_lastname
    tx_ref = "bKSt9302" + str(order.id)
    return render(request,'payments/payment_page.html', {'publicKey': publicKey, 'amount': amount, 'customer_email': customer_email, 'customerName': customer_Name, 'tx_ref':tx_ref})
