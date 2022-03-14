from django.urls import path

from app.views import cliente_views

urlpatterns = [
    path('cadastrar-cliente', cliente_views.cadastrar_cliente, name='cadastrar-cliente')
]
