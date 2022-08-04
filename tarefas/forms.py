from optparse import Option
from django import forms
from .models import Tarefa


class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('description', 'category')


class EditarTarefaForm(forms.Form):

    OPTIONS_CATEGORY = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito'),
    )

    tarefa = forms.CharField(max_length=400)
    category = forms.ChoiceField(choices=OPTIONS_CATEGORY)
