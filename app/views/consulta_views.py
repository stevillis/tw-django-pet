from typing import Tuple

from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from app.entidades import consulta
from app.forms import consulta_forms
from app.forms.consulta_forms import ConsultaForm
from app.services import consulta_service, pet_service
from app.utils.permissions import has_cargo_veterinario


def get_pet_cleaned_data(form_consulta: ConsultaForm) -> Tuple:
    motivo = form_consulta.cleaned_data.get('motivo')
    peso_atual = form_consulta.cleaned_data.get('peso_atual')
    medicacao_atual = form_consulta.cleaned_data.get('medicacao_atual')
    medicacao_prescrita = form_consulta.cleaned_data.get('medicacao_prescrita')
    exames_prescritos = form_consulta.cleaned_data.get('exames_prescritos')
    pet = form_consulta.cleaned_data.get('pet')

    return motivo, peso_atual, medicacao_atual, medicacao_prescrita, exames_prescritos, pet


@user_passes_test(lambda user: has_cargo_veterinario(user))
def cadastrar_consulta(request, pet_id):
    pet_bd = pet_service.listar_pet_id(pet_id)
    if request.method == 'POST':
        form_consulta = consulta_forms.ConsultaForm(request.POST)

        if form_consulta.is_valid():
            motivo, peso_atual, medicacao_atual, medicacao_prescrita, exames_prescritos, _ = get_pet_cleaned_data(
                form_consulta)

            consulta_nova = consulta.Consulta(motivo=motivo, peso_atual=peso_atual, medicacao_atual=medicacao_atual,
                                              medicacao_prescrita=medicacao_prescrita,
                                              exames_prescritos=exames_prescritos, pet=pet_bd)
            consulta_service.cadastrar_consulta(consulta_nova)

            return redirect('listar-pet-id', pet_id)
    else:
        form_consulta = consulta_forms.ConsultaForm()
    context = {
        'form_consulta': form_consulta,
        'pet_nome': pet_bd.nome,
        'is_edit': False
    }
    return render(request, 'consultas/form_consulta.html', context)


@login_required()
def listar_consulta_id(request, pk):
    consulta_bd = consulta_service.listar_consulta_por_id(pk)
    return render(request, 'consultas/lista_consulta.html', {'consulta': consulta_bd})


@login_required()
def enviar_email_consulta(request, pk):
    consulta_bd = consulta_service.listar_consulta_por_id(pk)
    pet_consulta = pet_service.listar_pet_id(consulta_bd.pet.id)
    assunto = 'Consulta do seu Pet'
    mensagem_html = render_to_string('consultas/consulta_email.html', {'consulta': consulta_bd})
    corpo_email = 'Resumo da consulta do seu Pet'
    email_remetente = settings.EMAIL_HOST_USER
    email_destino = (pet_consulta.dono.email,)
    send_mail(assunto, corpo_email, email_remetente, email_destino, html_message=mensagem_html)

    return redirect('listar-consulta-id', pk)
