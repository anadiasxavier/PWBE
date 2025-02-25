from django.urls import path
from . import views

urlpatterns = [
 path('', views.lista_tafera, name='lista_tarefa'),
]