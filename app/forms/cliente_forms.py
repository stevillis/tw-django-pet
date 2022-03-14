from django import forms
from django.forms import DateInput, TextInput

from app.models import Cliente


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'data_nascimento', 'cpf', 'profissao']
        widgets = {
            'data_nascimento': DateInput(attrs={'type': 'date'}),
            'cpf': TextInput(attrs={'data-mask': '000.000.000-00'})
        }
