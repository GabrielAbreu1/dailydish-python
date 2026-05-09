from utils import limpar_tela, exibir_nome_do_programa, exibir_opcoes
from menus import finalizar_app, opcao_invalida
from restaurantes import alternar_estado_restaurante, listar_restaurantes, cadastrar_novo_restaurante

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
                return True
            case 2:
                listar_restaurantes()
                return True
            case 3:
                alternar_estado_restaurante()
                return True
            case 4:
                finalizar_app()
                return False
            case _:
                opcao_invalida()
                return True

    except ValueError:
        opcao_invalida()
        return True


def main():
    """
    Função principal da aplicação.

    Inicializa o sistema exibindo o banner,
    o menu de opções e aguardando a escolha
    do usuário.
    """

    while True:
        limpar_tela()
        exibir_nome_do_programa()
        exibir_opcoes()
        continuar = escolher_opcao()
        if not continuar:
            break


if __name__ == '__main__':
    main()