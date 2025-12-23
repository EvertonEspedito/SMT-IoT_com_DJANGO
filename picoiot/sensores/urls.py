from django.urls import path
from . import views

urlpatterns = [
    path('grafico/', views.grafico, name='grafico'),
    path('api/dados/', views.dados_temperatura, name='dados'),
    path('api/temperatura/', views.receber_temperatura, name='receber'),
]
