# Desenvolva uma aplicação em Python, estruturada segundo o padrão de arquitetura MVC (Model–View–Controller) e utilizando orientação a objetos, para gerenciar um pequeno sistema de biblioteca universitária. O programa deve utilizar um banco de dados PostgreSQL com duas tabelas relacionadas. Uma tabela autor com id, nome e nacionalidade e outra tabela livro com id, título, ano de publicação e o id do autor do livro.

Ao iniciar o sistema, o usuário deve ver o seguinte menu principal:

Menu Principal

1. Gerenciar autor

2. Gerenciar livro

3. Sair

O programa deve retornar ao menu principal sempre após concluir uma operação.

Ao selecionar Gerenciar autor, exibir o submenu:

Gerenciar Autor

1. Cadastrar autor

2. Listar autores

3. Atualizar autor

4. Excluir autor

5. Voltar ao menu principal

O submenu deve permanecer em loop até o usuário escolher voltar.

Ao selecionar Gerenciar livro, exibir o submenu:

Gerenciar Livro

1. Cadastrar livro

2. Listar livros (mostrar o nome do autor associado)

3. Atualizar livro

4. Excluir livro

5. Voltar ao menu principal

Este submenu também deve funcionar em loop.
