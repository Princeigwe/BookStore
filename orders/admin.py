from django.contrib import admin
from .models import OrderItem, Order


# Register your models here.

## Here django admin dashboard is to show order details with order items line by line

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['bookName',]
    readonly_fields = ('bookName', 'quantity', 'unitPrice', 'totalPrice')
    
    
    
    
        

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_firstname', 'customer_lastname', 'address',
                    'telephone', 'email', 'dateCreated', 'paid']
    readonly_fields = ('id', 'customer_firstname', 'customer_lastname', 'address',
                    'telephone', 'email', 'dateCreated', 'paid', 'totalPrice',)
    
    list_filter = ['id', 'paid']
    
    inlines = [OrderItemInline]
    
    