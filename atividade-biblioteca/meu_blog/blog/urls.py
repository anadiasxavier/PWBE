from django.urls import path
from .import views
#essas são as urls que foram usadas nas views.
urlpatterns = [
    path('', views.lista_livro, name='lista_livro'),
    path('livro/', views.lista_create, name= 'lista_create'),
    path('livroparte2/<int:pk>/', views.lista_update, name='lista_update'),
    path('livroparte3/<int:pk>/', views.lista_delete, name= 'lista_delete'),
    path('livroparte4/', views.lista_livros, name= 'lista_livros'),
]