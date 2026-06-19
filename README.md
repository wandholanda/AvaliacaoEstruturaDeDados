# Sistema Escolar Django

## Os 8 erros que encontrei

**1. portal/models.py** — os models usam `timezone.now` como valor padrão das datas, só que o `timezone` nunca tinha sido importado. Sem isso o Django nem sobe, dá `NameError`. Resolvi importando `from django.utils import timezone` no topo do arquivo.

**2. portal/views.py** — na view `index`, o caminho do template estava `'templates/portal/index.html'`. O problema é que o Django já procura sozinho dentro da pasta `templates/`, então ficar repetindo isso no caminho faz ele não achar o arquivo. Tirei o "templates/" e deixei só `'portal/index.html'`.

**3. portal/forms.py** — o import do model tava `from models import Professor`, um caminho que não existe nesse projeto. Troquei pra `from portal.models import Professor`, que é o caminho certo já que o model fica dentro do app portal.

**4. sistema/urls.py** — na rota de cadastro, em vez de uma view tinha um texto solto em português (tipo "preciso mostrar a página cadastro.html"), o que nem é código Python e quebra o projeto inteiro na hora de subir. Troquei por `include('portal.urls')`, fazendo o urls.py do projeto principal jogar as rotas pro urls.py do app portal.

**5. portal/admin.py** — no `list_display` do ProfessorAdmin tinha o campo `'especialidade'`, só que esse campo não existe no model Professor. O campo certo é `'disciplina'`, então troquei.

**6. sistema/settings.py** — o app portal não tava registrado no `INSTALLED_APPS`. Sem isso o Django ignora os models, as migrations e os templates do app inteiro. Adicionei `'portal'` na lista.

**7. portal/models.py** — o campo `matricula` do model Aluno tava como `IntegerField()`. O problema é que matrícula pode começar com zero (tipo "0042"), e quando é número esse zero some (vira 42 e perde a informação). Troquei pra `CharField(max_length=10)`, que guarda exatamente como foi digitado.

**8. portal/urls.py** — a rota de cadastro chamava `views.cadastro`, mas essa view nunca tinha sido criada no views.py. Criei a view cadastro (e o template cadastro.html que ela usa) pra rota parar de dar erro.



## Como rodar o projeto localmente

```bash
# 1. Clone o repositório
git clone https://github.com/wandholanda/AvaliacaoEstruturaDeDados.git
cd sistema_escolar_django-main

# 2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
venv\Scripts\activate

# 3. Instale o Django
pip install django

# 4. Aplique as migrations
python manage.py migrate

# 5. Rode o servidor
python manage.py runserver
```

Depois é só acessar `http://127.0.0.1:8000/index/` no navegador.

---

`Wanderson Deodato Holanda`

