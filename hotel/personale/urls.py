from django.urls import path
from django.conf import settings
from .views import Index, Personale#, Beskriv#, Jul, Andet, Base, Hart, Star, Rund, Firkant, Sekskant
from django.views import View
from . import views
#from django.conf.urls.static import static

urlpatterns = [
  path('', Index.as_view(), name='index'),
  path('personale/', Personale.as_view(), name='personale'),
  path('reservation/', views.reservation, name='reservation'),
  path('middag/', views.middag, name='middag'),
  path('mangler/', views.mangler, name='mangler'),
  #path('stjerne/', Stjerne.as_view(), name='stjerne'),
  #path('jul/', Jul.as_view(), name='jul'),
  #path('andet/', Andet.as_view(), name='andet'),
  #path('base/', Base.as_view(), name='base'),
  #path('hart/', Hart.as_view(), name='hart'),
  #path('star/', Star.as_view(), name='star'),
  #path('rund/', Rund.as_view(), name='rund'),
  #path('firkant/', Firkant.as_view(), name='firkant'),
  #path('sekskant/', Sekskant.as_view(), name='sekskant'),




]