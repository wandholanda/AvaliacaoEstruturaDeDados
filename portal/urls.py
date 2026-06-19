from django.urls import path

from portal import views

# exemplo: path('index/', views.index)
urlpatterns = [
    path('index/', views.index),
    # ERRO ENCONTRADO: essa rota chamava views.cadastro, mas essa view ainda não existia em views.py
    # CORREÇÃO: criei a view cadastro lá no views.py, agora essa rota funciona
    path('cadastro/', views.cadastro),
]


# Verbos HTTP - FRONTEND <-> BACKEND
#  GET -> www.escola.com -> Exiba a página home da escola.
#  POST -> www.escola.com/cadastro -> Cadastrando um novo usuário.
#  PUT -> www.escola.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE -> www.escola.com/logado/deletar/1 -> Deletando um usuário.
