from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name ='index'),
  path('melde/', views.melde, name='melde'),
  path('update/<str:pk>', views.update, name="update"),
  path('komind/', views.komind, name='komind'),
]