from utils import exibir_subtitulo

def cancelar_operacao():

    """
    Cancela a operação atual do sistema.

    Exibe uma mensagem informando o cancelamento
    e retorna o usuário ao menu principal.
    """

    print('Operação cancelada.\n')
    input('\nPressione Enter para continuar.')


def opcao_invalida():
    """
    Exibe uma mensagem de erro para opções inválidas.

    Em seguida, retorna ao menu principal.
    """
    print('Opção inválida!\n')
    input('\nPressione Enter para continuar.')


def finalizar_app():
    """
    Exibe uma mensagem de encerramento.
    """
    exibir_subtitulo('Encerrando o programa') 