from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView

from inscricao.forms import InscricaoForm
from inscricao.models import Inscricao, Curso


def index(request):
    context = {'page_title': 'Minha página'}
    return render(request, template_name='index.html', context=context)


class CreateInscricao(CreateView):
    form_class = InscricaoForm
    template_name = 'form.html'
    success_url = reverse_lazy('comprovante')

    def form_valid(self, form):
        curso_outro = form.cleaned_data['curso_outro']
        self.object = form.save()
        if form.cleaned_data['curso'] is None:
            if curso_outro:
                curso, created = Curso.objects.get_or_create(nome=curso_outro)
                self.object.curso = curso
                self.object.save()

        send_mail(
            'Inscrição realizada com sucesso',
            render_to_string('email.html', context={'inscricao': self.object}),
            settings.EMAIL_HOST_USER,
            [self.object.email],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Formulário de inscrição'
        return context


def comprovante(request):
    context = {'page_title': 'Minha página', 'success': True}
    return render(request, template_name='index.html', context=context)
