from django.urls import path
from django.conf import settings
from .views import Index, Reservation#, Beskriv#, Jul, Andet, Base, Hart, Star, Rund, Firkant, Sekskant
from django.views import View
#from django.conf.urls.static import static

urlpatterns = [
  path('', Index.as_view(), name='index'),
  path('reservation/', Reservation.as_view(), name='reservation'),
 # path('beskriv/', Beskriv.as_view(), name='beskriv'),
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