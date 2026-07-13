import os

def limpar_tela():
   
    """
    Limpa a tela do terminal de forma compatível com Windows, Linux e Mac.                                                                 
    """
   
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_nome_do_programa():
    """
    Exibe o banner principal do sistema no terminal.

    Apresenta o nome do programa em ASCII Art,
    funcionando como tela inicial da aplicação.
    """
    print("""
██████╗░░█████╗░██╗██╗░░░░░██╗░░░██╗██████╗░██╗░██████╗██╗░░██╗
██╔══██╗██╔══██╗██║██║░░░░░╚██╗░██╔╝██╔══██╗██║██╔════╝██║░░██║
██║░░██║███████║██║██║░░░░░░╚████╔╝░██║░░██║██║╚█████╗░███████║
██║░░██║██╔══██║██║██║░░░░░░░╚██╔╝░░██║░░██║██║░╚═══██╗██╔══██║
██████╔╝██║░░██║██║███████╗░░░██║░░░██████╔╝██║██████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝░░░╚═╝░░░╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝
    """)


def exibir_opcoes():
    """
    Exibe o menu principal de opções.

    Mostra ao usuário as funcionalidades
    disponíveis no sistema.
    """
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Filtrar por Categoria')
    print('4. Alterar Status Restaurante')
    print('5. Excluir Restaurante')
    print('6. Sair\n')


def exibir_subtitulo(texto):
    """
    Exibe um subtítulo formatado no terminal.

    Args:
        texto (str): Texto a ser exibido como subtítulo.
    """
    limpar_tela()
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()