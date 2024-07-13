from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import listings, listing, create, update, delete


urlpatterns = [
    path('', listings, name='listings'),
    path('listing/<id>/', listing, name='listing'),
    path('create/', create, name='create'),
    path('update/<id>/', update, name='update'),
    path('delete/<id>/', delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)