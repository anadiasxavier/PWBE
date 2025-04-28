#é importado das views
from django.urls import path
from .import views

#na urlpatterns é definida a url do projeto 
urlpatterns = [
    path('criar/', view=views.criar_usuario, name='criar_usuario'),
    path('logar/', view=views.logar_usuario, name='logar_usuario'),
    path('read/', view=views.read, name= 'read'),
    path('update/<int:pk>', view=views.update_usuarios, name='update'),
    path('delete/<int:pk>', view=views.delete_usuarios, name='delete'),
]