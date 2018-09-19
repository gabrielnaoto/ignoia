from django.db import models

from inscricao.validators import validate_CPF


class Curso(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF', validators=[validate_CPF])
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    telefone = models.CharField(max_length=25, help_text='Exemplo: (XX) XXXXX-XXXX')
    curso = models.ForeignKey(Curso, verbose_name='Curso de graduação', blank=True, null=True,
                              on_delete=models.DO_NOTHING, help_text='Selecione um curso da lista')
    email = models.EmailField(verbose_name='E-mail',
                              help_text='Através deste endereço eletrônico você receberá sua confirmação de inscrição')
