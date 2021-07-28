from django.contrib import admin
from  .models import Wishlist, WishlistItem

# Register your models here.

class WishlistItemAdminInline(admin.TabularInline):
    model = WishlistItem
    list_display = ['book']
    readonly_fields =['book', 'date_created']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display= ['user']
    inlines = [WishlistItemAdminInline]

