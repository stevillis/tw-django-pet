from django import forms

from app.models import Consulta


class ConsultaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Consulta
        fields = '__all__'
        exclude = ['pet']
