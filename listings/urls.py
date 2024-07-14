from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import cars, car, create, update, delete, home


urlpatterns = [
    path('', home, name='home'),
    path('cars/', cars, name='listings'),
    path('cars/car/<id>/', car, name='listing'),
    path('cars/create/', create, name='create'),
    path('cars/update/<id>/', update, name='update'),
    path('cars/delete/<id>/', delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)