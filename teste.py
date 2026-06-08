class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {"Restaurante aberto" if self._ativo else "Restaurante fechado"}'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        

