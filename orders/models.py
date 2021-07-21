from django.db import models
from books.models import Book

# Create your models here.

class Order(models.Model):
    
    """an order model containing the customer first and last names and contact details.
    It also contains info on if the order has been paid for, and the date the order was created."""
    
    customer_firstname = models.CharField(max_length=100)
    customer_lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    dateCreated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-dateCreated',)
    
    def __str__(self):
        return self.customer_firstname
    
    
    def totalPrice(self):
        return sum(orderItem.item_total_price() for orderItem in self.orderItems.all())
    
    


class OrderItem(models.Model):
    
    """an orderItem model that contains info on thr book that was ordered.
    This model is tied to the Order model containing the customer ordering for it.
    It contains the item unit price, and the quantity of of the item ordered."""
    order = models.ForeignKey(Order, related_name='orderItems', on_delete=models.CASCADE)
    bookName = models.ForeignKey(Book, related_name='bookItem', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unitPrice = models.DecimalField(max_digits=10,decimal_places=2)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return str(self.bookName)
    
    
    def item_total_price(self):
        return self.unitPrice * self.quantity


