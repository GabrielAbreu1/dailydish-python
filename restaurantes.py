from utils import exibir_subtitulo
from menus import cancelar_operacao

restaurantes_cadastrados = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]


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
        nome_do_restaurante = input('Digite o nome do restaurante ou ("voltar" para cancelar a operação): ').strip()

        if nome_do_restaurante.lower() == 'voltar':
            cancelar_operacao()
            return

        if not nome_do_restaurante:
            print('O nome não pode estar vazio. Tente novamente.\n')
        else:
            break

    while True:
        categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante} ou ("voltar" para cancelar a operação): ').strip()

        if categoria.lower() == 'voltar':
            cancelar_operacao()
            return

        if not categoria:
            print(f'A categoria não pode estar vazia. Tente novamente.\n')
        else:
            break
        
    if verifica_restaurante_cadastrado(nome_do_restaurante, categoria, restaurantes_cadastrados):
        print(f'Restaurante {nome_do_restaurante} já cadastrado.\n')
        input('\nPressione Enter para continuar.')
        return
    

    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes_cadastrados.append(dados_do_restaurante)

    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso.\n')
    input('\nPressione Enter para continuar.')


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

    input('\nPressione Enter para continuar.')


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
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado ou ("voltar" para cancelar a operação): ').strip()

    restaurante_encontrado = False

    if nome_restaurante.lower() == 'voltar':
        cancelar_operacao()
        return

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

    input('\nPressione Enter para continuar.')