from django.urls import path
from . import views

#Aqui foi criadas as urls das views, depois elas foram utilizadas no postman.

urlpatterns = [
    path('carros/', views.read_carros),
    path('carros/buscar/<int:pk>', views.pegar_carro),
    path('carros/criar/', views.create_carro),
    path('carros/atualizar/<int:pk>', views.update_carro),
    path('carros/apagar/<int:pk>', views.delete_carro),
]