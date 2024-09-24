from rolepermissions.roles import AbstractUserRole


class Aluno(AbstractUserRole):
    available_permissions = {
        'ver_meu_perfil':True,
        'pegar_chave_armario':True,
        'requisitar_atendimento':True,
    }


class Professor(AbstractUserRole):
    available_permissions = {
        'gerenciar_perfil_alunos':True,
        'pegar_chave_armario':True,
        'responder_atendimento':True,
    }