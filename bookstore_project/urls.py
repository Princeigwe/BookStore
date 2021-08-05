"""bookstore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # import the static url from settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="BookStore API",
        default_version='v1',
        description="A simple BookStore API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="igwep297@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('admin/', admin.site.urls),
    # django user 
    path('accounts/', include('allauth.urls')),
    
    
    #local apps urls
    path('', include('pages.urls', namespace='pages')),
    path('books/', include('books.urls', namespace='books')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payments/', include('payments.urls', namespace='payments')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('api/app/', include('api.urls')),
    
    ## 3rd party urls
    # path('search/', include('haystack.urls')),
    path('api/api-auth/', include('rest_framework.urls')), ## rest_framework url
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')), ## django rest authentication urls
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), # django rest registration url
    
    path('swagger/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ## adding the media url and it's root


admin.site.site_header  =  "BookStore Admin"  # Custom BookStore Admin Header