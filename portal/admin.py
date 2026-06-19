from django.contrib import admin
from portal import models

@admin.register(models.Professor)  # Registrando a classe Professor no Portal do Django
class ProfessorAdmin(admin.ModelAdmin):
    # ERRO ENCONTRADO: o campo 'especialidade' não existe no model Professor, o nome certo é 'disciplina'
    # CORREÇÃO: troquei 'especialidade' por 'disciplina', que é o campo que realmente existe no models.py
    list_display = ('id', 'nome', 'email', 'telefone', 'disciplina', 'ativo',)

@admin.register(models.Aluno)  # Registrando a classe Aluno no Portal do Django
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Aula)  # Registrando a classe Aula no Portal do Django
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'professor_id', 'status',)
