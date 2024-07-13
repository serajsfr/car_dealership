from django.urls import path
from .views import listings, listing


urlpatterns = [
    path('', listings, name='listings'),
    path('listing/<id>/', listing, name='listing'),
]