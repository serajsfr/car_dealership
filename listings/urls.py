from django.urls import path
from .views import listings, listing, create, update, delete


urlpatterns = [
    path('', listings, name='listings'),
    path('listing/<id>/', listing, name='listing'),
    path('create/', create, name='create'),
    path('update/<id>/', update, name='update'),
    path('delete/<id>/', delete, name='delete'),
]