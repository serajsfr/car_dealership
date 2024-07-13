from django.urls import path
from .views import listings, listing, create


urlpatterns = [
    path('', listings, name='listings'),
    path('listing/<id>/', listing, name='listing'),
    path('create/', create, name='create'),
]