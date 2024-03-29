from django.urls import path
from django.conf import settings
from .views import Index, Info, Beskriv, Opleve, Kontakt, Afregn#, Menu
from django.views import View
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', Index.as_view(), name='index'),
  path('info/', Info.as_view(), name='info'),
  path('beskriv/', Beskriv.as_view(), name='beskriv'),
  path('opleve/', Opleve.as_view(), name='opleve'),
  path('reserver/', views.Reserver, name='reserver'),
  #path('update_reserver/<str:pk>', views.update_reserver, name='update_reserver'),
  path('kontakt/', Kontakt.as_view(), name='kontakt'),
  path('fejl/', views.fejl, name='fejl'),
  path('dinner/', views.dinner, name='dinner'),
  path('afregn/', Afregn.as_view(), name='afregn'),
  #path('rund/', Rund.as_view(), name='rund'),
  #path('firkant/', Firkant.as_view(), name='firkant'),
  #path('sekskant/', Sekskant.as_view(), name='sekskant'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)