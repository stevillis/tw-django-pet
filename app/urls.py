from django.urls import path

from app.views import cliente_views

urlpatterns = [
    path('cadastrar-cliente/', cliente_views.cadastrar_cliente, name='cadastrar-cliente'),
    path('listar-clientes/', cliente_views.listar_clientes, name='listar-clientes'),
    path('listar-cliente/<int:pk>/', cliente_views.listar_cliente_id, name='listar-cliente'),
    path('editar-cliente/<int:pk>/', cliente_views.editar_cliente, name='editar-cliente'),
    path('excluir-cliente/<int:pk>/', cliente_views.excluir_cliente, name='excluir-cliente')
]
