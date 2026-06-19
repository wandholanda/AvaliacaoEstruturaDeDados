from django.shortcuts import render

# GET, POST, PUT, DELETE
# REQUEST <-> RESPONSE
# RENDER -> RENDERIZAR

# CRIANDO UMA VIEW PARA APRESENTAR A PÁGINA INDEX - USE FUNÇÃO
def index(request):  # É a request feita pelo usuário
    # ERRO ENCONTRADO: o caminho do template estava 'templates/portal/index.html', mas o Django já procura sozinho dentro da pasta templates
    # CORREÇÃO: tirei o "templates/" do caminho, ficando só 'portal/index.html'
    return render(
        request,
        'portal/index.html'
    )

# ERRO ENCONTRADO: o urls.py chama views.cadastro, mas essa view nunca foi criada aqui
# CORREÇÃO: criei a view cadastro pra renderizar a página de cadastro, assim a rota deixa de dar erro
def cadastro(request):
    return render(
        request,
        'portal/cadastro.html'
    )
