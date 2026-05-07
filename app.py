import os

def limpar_tela():
   
    """
    Limpa a tela do terminal de forma compatível com Windows, Linux e Mac.
    """
   
    os.system('cls' if os.name == 'nt' else 'clear')



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
    limpar_tela()
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def cancelar_cadastro():

    """
    Cancela o processo de cadastro de restaurante.

    Exibe uma mensagem informando o cancelamento e
    retorna o usuário ao menu principal do sistema.
    """

    print('Cadastro cancelado.\n')
    voltar_ao_menu_principal()


def verifica_restaurante_cadastrado(nome, categoria, restaurantes_cadastrados):

    """
    Verifica se já existe um restaurante cadastrado com o mesmo nome e categoria.

    A comparação é feita ignorando diferenças de maiúsculas/minúsculas
    e espaços extras no início e fim das strings.

    Args:
        nome (str): Nome do restaurante a ser verificado.
        categoria (str): Categoria do restaurante.
        restaurantes_cadastrados (list): Lista de restaurantes já cadastrados.

    Returns:
        bool: True se já existir um restaurante com o mesmo nome e categoria,
              False caso contrário.
    """

    nome = nome.strip().lower()
    categoria = categoria.strip().lower()

    for restaurante in restaurantes_cadastrados:
        nome_existente = restaurante['nome'].strip().lower()
        categoria_existente = restaurante['categoria'].strip().lower()

        if nome_existente == nome and categoria_existente == categoria:
            return True

    return False

def cadastrar_novo_restaurante():

    """
    Cadastra um novo restaurante no sistema.

    Solicita o nome e a categoria do restaurante através do terminal,
    com validação para impedir entradas vazias ou inválidas.

    Durante o processo, o usuário pode digitar 'voltar' para cancelar
    o cadastro e retornar ao menu principal.

    O fluxo de cancelamento foi abstraído para evitar repetição de código
    (princípio DRY), centralizando o comportamento de encerramento do cadastro.

    Após a validação, os dados são armazenados em um dicionário e
    adicionados à lista de restaurantes cadastrados.
    """

    exibir_subtitulo('Cadastro de novos restaurantes')

    while True:
        nome_do_restaurante = input('Digite o nome do restaurante ou ("voltar" para cancelar o cadastro): ').strip()

        if nome_do_restaurante.lower() == 'voltar':
            cancelar_cadastro()
            return

        if not nome_do_restaurante:
            print('O nome não pode estar vazio. Tente novamente.\n')
        else:
            break

    while True:
        categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante} ou ("voltar" para cancelar o cadastro): ').strip()

        if categoria.lower() == 'voltar':
            cancelar_cadastro()
            return

        if not categoria:
            print(f'A categoria não pode estar vazia. Tente novamente.\n')
        else:
            break
        
    if verifica_restaurante_cadastrado(nome_do_restaurante, categoria, restaurantes_cadastrados):
        print(f'Restaurante {nome_do_restaurante} já cadastrado.\n')
        voltar_ao_menu_principal()
        return
    

    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes_cadastrados.append(dados_do_restaurante)

    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso.\n')
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
    Alterna o estado (ativo/inativo) de um restaurante cadastrado.

    O usuário informa o nome do restaurante, e o sistema realiza a busca
    na lista de restaurantes cadastrados.

    A comparação do nome é feita de forma case-insensitive (ignorando
    maiúsculas e minúsculas) e também desconsidera espaços extras,
    utilizando .strip() e .lower().

    Se o restaurante for encontrado, o campo 'ativo' é invertido:
    - True → False (desativa)
    - False → True (ativa)

    Caso o restaurante não seja encontrado, uma mensagem de erro é exibida.

    Não retorna valores.
    """
    
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ' ).strip()

    restaurante_encontrado = False

    for restaurante in restaurantes_cadastrados:
        if nome_restaurante.lower() == restaurante['nome'].strip().lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            if restaurante['ativo']:
                print(f'Restaurante {nome_restaurante} ativado com sucesso.\n')
            else:
                print(f'Restaurante {nome_restaurante} desativado com sucesso.\n')

            break

    if not restaurante_encontrado:
        print('Restaurante não encontrado.\n')

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
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()