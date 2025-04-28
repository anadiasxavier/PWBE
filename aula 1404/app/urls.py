from django.urls import path
from .views import PilotoListCreateAPIView, PilotoRetrieveUpdateDestroyAPIView
from .views import CarroListCreateAPIView, CarroRetrieveUpdateDestroyAPIView
#urlpatterns serve para criar as urls utilizando as views
urlpatterns = [
    #criando as urls
    path('piloto/', view=PilotoListCreateAPIView.as_view()),
    path('piloto/<int:pk>', view=PilotoRetrieveUpdateDestroyAPIView.as_view()),
    path('carro/', view=CarroListCreateAPIView.as_view()),
    path('carro/<int:pk>', view=CarroRetrieveUpdateDestroyAPIView.as_view()),
    
]