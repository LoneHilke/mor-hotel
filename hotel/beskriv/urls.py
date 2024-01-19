from django.urls import path
from django.conf import settings
from .views import Beskriv
from info.views import Index
from django.views import View
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/', Index.as_view(), name='index'),
    path('beskriv/', Beskriv.as_view(), name='beskriv'),
  
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)