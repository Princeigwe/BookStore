from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WishlistConfig(AppConfig):
    name = 'wishlist'
    verbose_name = _('wishlist')
    
    def ready(self):
        import wishlist.signals
