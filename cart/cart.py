from decimal import Decimal
from django.conf import settings
from books.models import Book

class Cart():
    
    # initializing the cart class
    def __init__(self, request):
        self.session = request.session ## assigning django session to self.session
        cart = self.session.get(settings.CART_SESSION_ID) # retrieving the cart session ID and assigning it to the 'cart' variable
        
        if not cart: # if no cart is present...
            cart = self.session[settings.CART_SESSION_ID] = {} # create an empty cart
        
        self.cart = cart
    
    # function for adding book quantity to cart or overriding the quantity
    def addBook(self, book, quantity=1, override_quantity=False):
        book_id = str(book.id)
        
        if book_id not in self.cart: # if the book id is not in the cart
            self.cart[book_id] = {'quantity': 0, 'price': str(book.price)} # create a book id key with zero quantity, and its price
        
        if override_quantity: # if override quantity property is not changed...
            self.cart[book_id]['quantity'] = quantity # set book id quantity to 1 
        
        else: # if override quantity is changed to True...
            self.cart[book_id]['quantity'] += quantity # increase book id quantity by 1
        self.save() # save the cart
    
    def save(self): ## function to apply changes
        self.session.modified = True
    
    # function to remove book from the cart
    def removeBook(self, book):
        book_id = str(book.id)
        
        if book_id in self.cart:
            del self.cart[book_id]
        self.save()
    
    # function to iterate through books in the cart
    def __iter__(self):
        book_ids = self.cart.keys()
        
        books = Book.objects.filter(id__in=book_ids) # filter book objects whose id is a key in the cart
        cart = self.cart.copy()
        
        for book in books:
            cart[str(book.id)]['book'] = book # create a book id key and give it its value
        
        for item in cart.values(): # for each book item key in the cart
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    # function to get total number of items in the cart
    def __len__(self):
        return sum( item['quantity'] for item in self.cart.values() )
    
    #function to get total price
    def total_price(self):
        return sum( Decimal(item['total_price'])  for item in self.cart.values() )
    
    # function to clear cart
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()