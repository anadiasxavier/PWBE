from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_read, name= 'item_read'),
    path('bruno/', views.item_crate, name='item_create'),
    path('giovana/<int:pk>/', views.item_update, name='item_upadate'),
    path('adrian/<int:pk>/', views.item_delete, name= 'item_delete'),

]