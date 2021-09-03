from django.db.models import fields
from django.forms import ModelForm
from .models import Transacao

class TransacaoForm(ModelForm):

    class Meta:
        model = Transacao
        fields = ['descricao','data', 'valor', 'categoria', 'observacoes']
        