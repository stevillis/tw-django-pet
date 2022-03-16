from django import template

from app.utils import permissions

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='has_cargo_veterinario')
def has_cargo_veterinario(user):
    return permissions.has_cargo_veterinario(user)


@register.filter(name='has_cargo_financeiro')
def has_cargo_financeiro(user):
    return permissions.has_cargo_financeiro(user)


@register.filter(name='has_cargo_atendimento')
def has_cargo_atendimento(user):
    return permissions.has_cargo_atendimento(user)
