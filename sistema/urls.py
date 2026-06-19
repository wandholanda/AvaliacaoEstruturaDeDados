from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ERRO ENCONTRADO: essa linha tinha um texto em português solto no lugar da view, isso nem é código Python válido
    # CORREÇÃO: troquei por include('portal.urls'), assim o Django manda as rotas /cadastro/ e /index/ pro urls.py do app portal
    path('', include('portal.urls')),
]


# Verbos HTTP - FRONTEND <-> BACKEND
#  GET -> www.escola.com -> Exiba a página home da escola.
#  POST -> www.escola.com/cadastro -> Cadastrando um novo usuário.
#  PUT -> www.escola.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE -> www.escola.com/logado/deletar/1 -> Deletando um usuário.
