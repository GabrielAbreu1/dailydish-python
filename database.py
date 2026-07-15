import sqlite3

def inicializar_banco():
	"""
    Inicializa o banco de dados da aplicação.

    Cria o arquivo do banco de dados SQLite, caso ele ainda não exista,
    e garante a criação da tabela `restaurantes` com sua estrutura
    padrão. Caso a tabela já exista, nenhuma alteração é realizada.

    Returns:
    None
	"""
 
	conexao = sqlite3.connect('dailydish.db')

	cursor = conexao.cursor()

	cursor.execute("""
	CREATE TABLE IF NOT EXISTS restaurantes(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT NOT NULL,
		categoria TEXT NOT NULL,
		ativo INTEGER DEFAULT 0
	)
	""")

	conexao.commit()

	conexao.close()
 
def salvar_restaurante(restaurante):
    
	"""
    Persiste um restaurante no banco de dados.

    Recebe um objeto Restaurante e insere seus dados na tabela
    `restaurantes`, armazenando o nome, a categoria e o estado de
    ativação.

    Args:
        restaurante (Restaurante): Instância da classe Restaurante
            contendo os dados a serem armazenados.

    Returns:
    None
	"""
    
	conexao = sqlite3.connect('dailydish.db')

	cursor = conexao.cursor()
 
	cursor.execute("""
    INSERT INTO restaurantes (nome, categoria, ativo)
    VALUES (?, ?, ?)
    """, (restaurante.nome, restaurante.categoria, restaurante.ativo))

	conexao.commit()
	conexao.close()
 
def carregar_restaurantes(): 
	"""
	Carrega todos os restaurantes cadastrados no banco de dados.

	Realiza uma consulta à tabela `restaurantes` e retorna uma lista
	de tuplas contendo os dados de cada restaurante, no formato:
	(id, nome, categoria, ativo).

	A conversão dessas tuplas em objetos Restaurante é realizada
	pelo módulo responsável pelas regras de negócio.

	Returns:
		list[tuple]: Lista de tuplas com os restaurantes
		cadastrados no banco de dados.
	"""

	conexao = sqlite3.connect('dailydish.db')

	cursor = conexao.cursor()

	cursor.execute("""
	SELECT * FROM restaurantes
	""")

	tabela = cursor.fetchall()

	conexao.close()

	return tabela


def excluir_restaurante_banco(restaurante):
    """
    Remove um restaurante do banco de dados.

    Exclui da tabela `restaurantes` o registro correspondente ao
    restaurante informado, utilizando o nome e a categoria como
    critérios de identificação.

    Args:
        restaurante (Restaurante): Instância da classe Restaurante
            que será removida do banco de dados.

    Returns:
        None
    """
    
    conexao = sqlite3.connect('dailydish.db')
    
    cursor = conexao.cursor()
    
    cursor.execute("""
    DELETE FROM restaurantes WHERE nome = ? AND categoria = ?
    """, (restaurante.nome, restaurante.categoria))
    
    conexao.commit()
    conexao.close()
    
    
def atualizar_estado_banco(restaurante):
    """
    Atualiza o estado de ativação de um restaurante no banco de dados.

    Localiza o restaurante na tabela `restaurantes` utilizando o nome
    e a categoria como critérios de identificação e atualiza o valor
    do campo `ativo` de acordo com o estado atual do objeto.

    Args:
        restaurante (Restaurante): Instância da classe Restaurante
            contendo o novo estado de ativação.

    Returns:
        None
    """
    
    conexao = sqlite3.connect('dailydish.db')
    
    cursor = conexao.cursor()
    
    cursor.execute("""
    UPDATE restaurantes SET ativo = ? WHERE nome = ? AND categoria = ?       
    """, (restaurante.ativo, restaurante.nome, restaurante.categoria))
    
    conexao.commit()
    conexao.close()