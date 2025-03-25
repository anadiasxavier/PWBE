from django.urls import path
from . import views

#Aqui foi criadas as urls das views, depois elas foram utilizadas no postman.

urlpatterns = [
    path('eventos/', views.categorias_eventos),
    path('eventos/buscar/<int:pk>', views.pegar_eventos),
    path('eventos/criar/', views.create_evento),
    path('eventos/atualizar/<int:pk>', views.update_evento),
    path('eventos/apagar/<int:pk>', views.delete_evento),
    path('eventos/proximos', views.ordem_eventos),
]