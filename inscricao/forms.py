from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field, HTML
from django import forms

from inscricao.models import Inscricao


class InscricaoForm(forms.ModelForm):
    curso_outro = forms.CharField(max_length=50, required=False, label='Outro',
                                  help_text='Informe o nome do seu curso')

    class Meta:
        model = Inscricao
        fields = '__all__'

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        helper.layout = Layout(
            Div(
                Div(
                    Field('cpf'),
                    css_class='col'
                ),
                css_class='row'

            ),
            Div(
                Div(
                    Field('nome'),
                    css_class='col'
                ),
                css_class='row'

            ),
            Div(
                Div(
                    Field('email'),
                    css_class='col'
                ),
                css_class='row'

            ),
            Div(
                Div(
                    Field('data_nascimento'),
                    css_class='col'
                ),
                css_class='row'

            ),
            Div(
                Div(
                    Field('telefone'),
                    css_class='col'
                ),
                css_class='row'

            ),
            Div(
                HTML(
                    '<strong>Atenção!</strong><br/>'
                    'Você deverá apenas informar um dos campos abaixo. Selecione um item da lista ou caso não encontrar o seu curso informe o nome de outro curso de graduação.'
                ),
                css_class='alert alert-info'

            ),
            Div(
                Div(
                    Field('curso'),
                    css_class='col'
                ),
                Div(
                    Field('curso_outro'),
                    css_class='col'
                ),
                css_class='row'

            ),
        )
        return helper
