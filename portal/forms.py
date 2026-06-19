from django import forms

# ERRO ENCONTRADO: import "from models import Professor" está errado, esse caminho não existe no projeto
# CORREÇÃO: trocado para "from portal.models import Professor", que é o caminho certo dentro do app portal
from portal.models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:  # A classe meta serve para configurar o form
        model = Professor  # Define o model que o form representa
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
