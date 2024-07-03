from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.sala, name='sala'),
    path('cadeiras', views.cadeiras, name='cadeiras')
]
