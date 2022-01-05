from django.urls import include, path

from cadastros.views import lista_cidades, detalhe_cidade, cadastra_cidade, remove_cidade, editar_cidade

urlpatterns = [
    path('', lista_cidades, name='cidades-list'),
    path('detalhe/<int:id>/', detalhe_cidade, name='cidades-detalhe'),
    path('create/', cadastra_cidade, name='cidades-cadastro'),
    path('delete/<int:id>/', remove_cidade, name='cidades-remove'),
    path('update/<int:id>/', editar_cidade, name='cidades-editar'),
]