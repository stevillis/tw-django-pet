from django.urls import path

from app.views import cliente_views, consulta_views, pet_views

urlpatterns = [
    path('cadastrar-cliente/', cliente_views.cadastrar_cliente, name='cadastrar-cliente'),
    path('listar-clientes/', cliente_views.listar_clientes, name='listar-clientes'),
    path('listar-cliente/<int:pk>/', cliente_views.listar_cliente_id, name='listar-cliente'),
    path('editar-cliente/<int:pk>/', cliente_views.editar_cliente, name='editar-cliente'),
    path('excluir-cliente/<int:pk>/', cliente_views.excluir_cliente, name='excluir-cliente'),

    path('cadastrar-pet/<int:cliente_id>/', pet_views.cadastrar_pet, name='cadastrar-pet'),
    path('listar-pet/<int:pk>/', pet_views.listar_pet_id, name='listar-pet-id'),

    path('cadastrar-consulta/<int:pet_id>/', consulta_views.cadastrar_consulta, name='cadastrar-consulta'),
    path('listar-consulta/<int:pk>/', consulta_views.listar_consulta_id, name='listar-consulta-id'),
]
