from app.models import (CARGO_ATENDIMENTO_CHOICE, CARGO_FINANCEIRO_CHOICE,
                        CARGO_VETERINARIO_CHOICE)


def has_cargo_veterinario(user):
    return user.cargo == CARGO_VETERINARIO_CHOICE


def has_cargo_financeiro(user):
    return user.cargo == CARGO_FINANCEIRO_CHOICE


def has_cargo_atendimento(user):
    return user.cargo == CARGO_ATENDIMENTO_CHOICE
