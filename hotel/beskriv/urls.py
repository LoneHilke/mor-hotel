from django.urls import path
from django.conf import settings
from .views import Beskriv
from django.views import View
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('beskriv/', Beskriv.as_view(), name='beskriv'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)