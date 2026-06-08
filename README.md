# DailyDish

Sistema de gerenciamento de restaurantes desenvolvido em Python com foco em organização de código, modularização e boas práticas de desenvolvimento.

---

## Sobre o projeto

O DailyDish é um projeto criado para praticar conceitos fundamentais de desenvolvimento back-end e arquitetura de software utilizando Python.

O sistema permite cadastrar, listar e gerenciar restaurantes através de um menu interativo no terminal, aplicando validações, regras de negócio e orientação a objetos para tornar o fluxo mais consistente e escalável.

Além das funcionalidades, o projeto também possui foco em:

- refatoração;
- reutilização de código;
- separação de responsabilidades;
- legibilidade;
- escalabilidade futura.

---

## Funcionalidades

- Cadastro de restaurantes com categorias pré-definidas
- Listagem de restaurantes cadastrados
- Filtro de restaurantes por categoria
- Alternância de status (aberto/fechado)
- Validação de duplicidade
- Cancelamento de operações
- Tratamento de entradas do usuário
- Menu interativo
- Modularização do sistema
- Normalização de nomes com title case

---

## Tecnologias utilizadas

- Python 3.12

---

## Estrutura do projeto

```text
dailydish-python/
├── app.py           — loop de eventos principal
├── menus.py         — navegação e fluxo do sistema
├── restaurantes.py  — classe Restaurante e regras de negócio
├── utils.py         — funções utilitárias
└── README.md
```

---

## Arquitetura

O projeto segue uma arquitetura em camadas onde cada módulo tem uma responsabilidade clara:

```
utils.py → menus.py → restaurantes.py → app.py
```

Cada camada só importa da camada abaixo — sem imports circulares.

---

## Conceitos aplicados

- DRY (Don't Repeat Yourself)
- Orientação a Objetos (POO)
- Encapsulamento com atributos privados
- Properties e type hints
- Modularização e separação de responsabilidades
- Arquitetura em camadas
- Refatoração de código
- Validação de dados
- Padronização de mensagens
- Loop de eventos

---

## Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/GabrielAbreu1/dailydish-python.git
```

2. Acesse a pasta do projeto:
```bash
cd dailydish-python
```

3. Execute o sistema:
```bash
python app.py
```

---

## Roadmap futuro

- Persistência de dados com SQLite
- Sistema de avaliação de restaurantes
- API REST com Flask
- Sistema de autenticação
- Interface web com Bootstrap
- Testes automatizados com pytest
- Deploy da aplicação

---

## Objetivo do projeto

O objetivo do DailyDish é evoluir gradualmente de um sistema em terminal para uma aplicação web completa, aplicando conceitos reais de desenvolvimento de software ao longo de cada etapa do projeto.

---

## Autor

Gabriel Abreu
- LinkedIn: https://www.linkedin.com/in/gabriel-abreu-65765a333/
- GitHub: https://github.com/GabrielAbreu1
