from django import forms
from django.forms import DateInput

from app.models import Funcionario


class FuncionarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Funcionario
        fields = ['nome', 'data_nascimento', 'cargo']
        widgets = {
            'data_nascimento': DateInput(attrs={'type': 'date'})
        }
