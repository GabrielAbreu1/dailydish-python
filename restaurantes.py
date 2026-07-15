from __future__ import annotations
from utils import exibir_subtitulo
from menus import cancelar_operacao
from database import salvar_restaurante, carregar_restaurantes, excluir_restaurante_banco, atualizar_estado_banco

class Restaurante:
    restaurantes_cadastrados: list['Restaurante'] = []
    
    def __init__(self, nome, categoria, ativo=False):
        self._nome = nome
        self._categoria = categoria
        self._ativo = bool(ativo)
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def ativo(self):
        return self._ativo
    
    @property
    def status(self):
        """Retorna o estado de funcionamento do restaurante."""
        
        return 'Restaurante aberto' if self.ativo else 'Restaurante fechado'
    
    def __str__(self):
        """
        Retorna uma representação textual do restaurante.
        Returns:
        str: Nome, categoria e status do restaurante.
        """
        
        return f'{self.nome} | {self.categoria} | {self.status}'
    
    def alternar_estado(self):
        """
        Alterna o estado de funcionamento do restaurante.
        Inverte o valor do atributo _ativo:
        - True para False
        - False para True
        """
        
        self._ativo = not self._ativo

    
CATEGORIAS = [
    'Pizza',
    'Hambúrguer',
    'Japonesa',
    'Brasileira',
    'Italiana',
    'Lanches',
    'Doces',
    'Padaria',
    'Cafeteria',
    'Salgados',
    'Churrasco',
    'Saudável',
    'Vegetariana',
    'Vegana',
    'Mexicana',
    'Árabe',
    'Chinesa',
    'Pastel',
    'Sorvetes',
    'Peixes e Frutos do Mar',
    'Bebidas',
    'Comida Regional',
    'Marmita'
]

def carregar_restaurantes_do_banco():
    lista_restaurantes = carregar_restaurantes()
    
    for restaurante in lista_restaurantes:
        novo_restaurante = Restaurante(restaurante[1], restaurante[2], restaurante[3])
        Restaurante.restaurantes_cadastrados.append(novo_restaurante)
    
    

def verifica_restaurante_cadastrado(nome, categoria, restaurantes_cadastrados):

    """
    Verifica se um restaurante com o mesmo nome e categoria já está cadastrado.

    Args:
        nome (str): Nome do restaurante.
        categoria (str): Categoria do restaurante.
        restaurantes_cadastrados (list[Restaurante]): Restaurantes cadastrados.

    Returns:
        bool: True se o restaurante já existir, False caso contrário.
    """

    nome_normalizado = nome.strip().lower()
    categoria_normalizada = categoria.strip().lower()

    for restaurante in restaurantes_cadastrados:
        nome_existente = restaurante.nome.strip().lower()
        categoria_existente = restaurante.categoria.strip().lower()

        if nome_existente == nome_normalizado and categoria_existente == categoria_normalizada:
            return True

    return False


def escolher_categoria():
    
    """
    Exibe as categorias disponíveis cadastradas no sistema e permite ao usuário escolher uma opção.

    As categorias são obtidas da constante global CATEGORIAS e apresentadas
    de forma enumerada no terminal.

    O usuário deve selecionar uma categoria digitando o número correspondente.

    Durante o processo, é possível cancelar a operação digitando 'voltar',
    retornando ao menu principal do sistema.

    Returns:
        str: Categoria escolhida pelo usuário.
        None: Caso a operação seja cancelada.
    """

    while True:
        for indice, categoria in enumerate(CATEGORIAS, start=1):
            print(f'{indice} - {categoria}')
        
        opcao = input('\nEscolha uma categoria ou ("voltar" para cancelar a operação): ').strip()
            
        if opcao.lower() == 'voltar':
            cancelar_operacao()
            return None

        try:
            escolha = int(opcao)
            
            if 1 <= escolha <= len(CATEGORIAS):

                categoria_escolhida = CATEGORIAS[escolha - 1]

                print(f'\nCategoria escolhida: {categoria_escolhida}')
                return categoria_escolhida
            
            else:
                print('\nOpção inválida.\n')

        except ValueError:
            print('\nDigite apenas números.\n')

def cadastrar_novo_restaurante():

    """
    Realiza o cadastro de um novo restaurante no sistema.

    O processo solicita o nome do restaurante e a categoria escolhida
    pelo usuário, validando:
    - nome não vazio;
    - categoria válida;
    - inexistência de cadastro duplicado.

    Caso todas as validações sejam aprovadas, uma nova instância de
    Restaurante é criada, adicionada à lista de restaurantes cadastrados
    e persistida no banco de dados SQLite.

    O usuário pode cancelar a operação antes da conclusão do cadastro.

    Returns:
    None
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
            nome_do_restaurante = nome_do_restaurante.title()
            break


    categoria = escolher_categoria()
    
    if categoria is None:
        return
        
    if verifica_restaurante_cadastrado(nome_do_restaurante, categoria, Restaurante.restaurantes_cadastrados):
        print(f'Restaurante {nome_do_restaurante} já cadastrado.\n')
        input('\nPressione Enter para continuar.')
        return
    

    novo_restaurante = Restaurante(nome_do_restaurante, categoria)

    Restaurante.restaurantes_cadastrados.append(novo_restaurante)
    salvar_restaurante(novo_restaurante)

    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso.\n')
    input('\nPressione Enter para continuar.')


def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados.

    Exibe em formato de tabela o nome, a categoria
    e o status dos objetos Restaurante armazenados
    em Restaurante.restaurantes_cadastrados.
    """
    exibir_subtitulo('Listando os Restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')

    for restaurante in Restaurante.restaurantes_cadastrados:

        print(
            f'- {restaurante.nome.ljust(20)} | '
            f'{restaurante.categoria.ljust(20)} | '
            f'{restaurante.status}'
        )

    input('\nPressione Enter para continuar.')
    
    
def listar_restaurantes_por_categoria():
    """
    Exibe os restaurantes cadastrados de uma categoria específica.

    Solicita ao usuário a escolha de uma categoria e lista todos os
    restaurantes pertencentes a ela, mostrando nome, categoria e status.

    Caso nenhum restaurante seja encontrado na categoria selecionada,
    uma mensagem informativa é exibida.

    O usuário pode cancelar a operação durante a seleção da categoria.

    Returns:
        None
    """
    exibir_subtitulo('Filtrando Restaurantes por Categoria')
    categoria_restaurante = escolher_categoria()
    
    if categoria_restaurante is None:
        return
    
    lista_restaurante_categoria = []
    
    for restaurante in Restaurante.restaurantes_cadastrados:
        
        if categoria_restaurante.lower() == restaurante.categoria.strip().lower():
            lista_restaurante_categoria.append(restaurante)


    if not lista_restaurante_categoria:
        print('Nenhum restaurante encontrado nessa categoria.\n')
    else:
        print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
        for restaurante in lista_restaurante_categoria:
            print(
            f'- {restaurante.nome.ljust(20)} | '
            f'{restaurante.categoria.ljust(20)} | '
            f'{restaurante.status}'
             )
    input('\nPressione Enter para continuar.')
    
    
def alternar_estado_restaurante():
    """
    Alterna o estado de ativação de um restaurante cadastrado.

    Solicita o nome do restaurante e exibe todos os restaurantes
    encontrados com esse nome para que o usuário escolha qual registro
    deseja alterar.

    Após a seleção, solicita uma confirmação. Caso a operação seja
    confirmada, o estado do restaurante é alternado entre ativo e
    inativo, sendo a alteração refletida tanto na lista de restaurantes
    cadastrados quanto no banco de dados SQLite.

    O usuário pode cancelar a operação a qualquer momento.

    Returns:
        None
    """
    
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado ou ("voltar" para cancelar a operação): ').strip()

    lista_restaurantes_encontrados = []
    
    if nome_restaurante.lower() == 'voltar':
        cancelar_operacao()
        return

    for restaurante in Restaurante.restaurantes_cadastrados:

        if nome_restaurante.lower() == restaurante.nome.strip().lower():
            lista_restaurantes_encontrados.append(restaurante)

        
    if not lista_restaurantes_encontrados:
        print('Restaurante não encontrado.\n')
    else: 
        print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(22)} | Status')
        for indice, restaurante in enumerate(lista_restaurantes_encontrados, start=1):
            print(f'{indice} - {restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.status}')

        while True:

            restaurante_alternar = input('Digite o numero do restaurante que deseja alterar o estado ou ("voltar" para cancelar a operação)' ).strip()
            
            if restaurante_alternar.lower() == 'voltar':
                cancelar_operacao()
                return
            
            try:
                escolha_alternar = int(restaurante_alternar)
                if 1 <= escolha_alternar <= len(lista_restaurantes_encontrados):
                    restaurante_escolhido = lista_restaurantes_encontrados[escolha_alternar - 1]
                    
                    confirmacao = input(f'Confirmar a alteração de estado do {restaurante_escolhido.nome}? (s/n): ').strip().lower()
                    
                    if confirmacao == 's':
                        restaurante_escolhido.alternar_estado()
                        atualizar_estado_banco(restaurante_escolhido)
                        print(f'Restaurante {restaurante_escolhido.nome} {restaurante_escolhido.status}. \n')
                        break
                    else:
                        print('Alternação cancelada. \n')        
                else:
                    print('\nOpção inválida. \n')
            except ValueError:
                print('\nDigite apenas números. \n')

    input('\nPressione Enter para continuar.')
    
def deletar_restaurante():
    """
    Remove um restaurante cadastrado do sistema.

    Solicita o nome do restaurante a ser excluído e exibe todos os
    restaurantes encontrados com esse nome para que o usuário escolha
    qual registro deseja remover.

    Antes da exclusão, solicita uma confirmação do usuário. Caso a
    operação seja confirmada, o restaurante é removido da lista de
    restaurantes cadastrados e do banco de dados SQLite.

    O usuário pode cancelar a operação a qualquer momento.

    Returns:
        None
    """
    
    exibir_subtitulo('Excluir restaurante cadastrado')
    nome_restaurante = input('Digite o nome do restaurante que deseja excluir ou ("voltar" para cancelar a operação)').strip()
    
    if nome_restaurante.lower() == 'voltar':
        cancelar_operacao()
        return
    
    lista_excluir_restaurante = []
    
    for restaurante in Restaurante.restaurantes_cadastrados:
        
        if nome_restaurante.lower() == restaurante.nome.strip().lower():
            lista_excluir_restaurante.append(restaurante)
            
    if not lista_excluir_restaurante:
        print('Nenhum restaurante encontrado com esse nome.\n')
        input('\nPressione Enter para continuar.')
    else:
        print(f'{"Nome do restaurante".ljust(22)} | Categoria')
        for indice, restaurante in enumerate(lista_excluir_restaurante, start=1):
            print(f'{indice} - {restaurante.nome.ljust(20)} | {restaurante.categoria}')
            
        while True:

            restaurante_excluir = input('Digite o numero do restaurante que deseja excluir ou ("voltar" para cancelar a operação)').strip()
            
            if restaurante_excluir.lower() == 'voltar':
                cancelar_operacao()
                return
            
            try:
                escolha_excluir = int(restaurante_excluir)
                if 1 <= escolha_excluir <= len(lista_excluir_restaurante):
                    restaurante_escolhido = lista_excluir_restaurante[escolha_excluir - 1]
                    
                    confirmacao = input(f'Confirmar a exclusão de {restaurante_escolhido.nome}? (s/n): ').strip().lower()
                    
                    if confirmacao == 's':
                        Restaurante.restaurantes_cadastrados.remove(restaurante_escolhido)
                        excluir_restaurante_banco(restaurante_escolhido)
                        print('Restaurante excluido com sucesso. \n')
                        break
                    else:
                        print('Exclusão cancelada. \n')        
                else:
                    print('\nOpção inválida. \n')
            except ValueError:
                print('\nDigite apenas números. \n')
        input('\nPressione Enter para continuar.')