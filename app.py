import os

restaurantes_cadastrados = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]

def exibir_nome_do_programa():
    """
    Exibe o banner principal do sistema no terminal.

    Apresenta o nome do programa em ASCII Art,
    funcionando como tela inicial da aplicação.
    """
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)


def exibir_opcoes():
    """
    Exibe o menu principal de opções.

    Mostra ao usuário as funcionalidades
    disponíveis no sistema.
    """
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Status Restaurante')
    print('4. Sair\n')


def finalizar_app():
    """
    Encerra a execução da aplicação.

    Exibe uma mensagem de encerramento.
    """
    exibir_subtitulo('Encerrando o programa')


def voltar_ao_menu_principal():
    """
    Aguarda interação do usuário e retorna ao menu principal.
    """
    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def opcao_invalida():
    """
    Exibe uma mensagem de erro para opções inválidas.

    Em seguida, retorna ao menu principal.
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """
    Exibe um subtítulo formatado no terminal.

    Args:
        texto (str): Texto a ser exibido como subtítulo.
    """
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante no sistema.

    Solicita o nome e a categoria do restaurante,
    cria um dicionário com os dados informados
    e adiciona à lista de restaurantes.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes_cadastrados.append(dados_do_restaurante)

    print(f'Restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados.

    Exibe nome, categoria e status de cada
    restaurante armazenado no sistema.
    """
    exibir_subtitulo('Listando os Restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')

    for restaurante in restaurantes_cadastrados:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Restaurante aberto' if restaurante['ativo'] else 'Restaurante fechado'

        print(
            f'- {nome_restaurante.ljust(20)} | '
            f'{categoria_restaurante.ljust(20)} | '
            f'{ativo}'
        )

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """
    Alterna o status de um restaurante.

    Permite ativar ou desativar um restaurante
    com base no nome informado pelo usuário.
    """
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alternar o estado: '
    )

    restaurante_encontrado = False

    for restaurante in restaurantes_cadastrados:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            if restaurante['ativo']:
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso')
            else:
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso')

            break

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado\n')

    voltar_ao_menu_principal()


def escolher_opcao():
    """
    Lê e processa a opção escolhida pelo usuário.

    Direciona a execução para a funcionalidade
    correspondente ao item selecionado.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()

    except ValueError:
        opcao_invalida()


def main():
    """
    Função principal da aplicação.

    Inicializa o sistema exibindo o banner,
    o menu de opções e aguardando a escolha
    do usuário.
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()