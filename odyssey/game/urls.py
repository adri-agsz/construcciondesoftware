from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('adrian', views.adrian, name = 'regla'),
    path('proceso', views.proceso, name = 'proceso'),
    path('bienvenida', views.bienvenida, name = 'bienvenida'),
    path('multiplicacion', views.multiplicacion, name = 'multiplicacion'),
    path('division', views.division, name = 'division'),
]

