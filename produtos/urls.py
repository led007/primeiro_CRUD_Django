

from django.urls import path
from .views import lista_produtos, detalhes_produto, novo_produto, editar_produto, deletar_produto

urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('produto/<int:pk>/', detalhes_produto, name='detalhes_produto'),
    path('produto/novo/', novo_produto, name='novo_produto'),
    path('produto/<int:pk>/editar/', editar_produto, name='editar_produto'),
    path('produto/<int:pk>/deletar/', deletar_produto, name='deletar_produto'),
]
