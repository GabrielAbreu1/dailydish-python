import sqlite3

def inicializar_banco():
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