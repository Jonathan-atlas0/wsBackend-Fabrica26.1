from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('limpar/', views.limpar_historico, name='limpar_historico'),
    path('ip/', views.buscar_ip, name='buscar_ip'),
]