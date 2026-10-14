from model.livro import Livro
from view.livro_view import LivroView

class LivroController:
    @staticmethod
    def gerenciar():
        while True:
            LivroView.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                titulo = input("Título: ")
                ano = input("Ano de publicação: ")
                autor_id = input("ID do autor: ")
                Livro.cadastrar(titulo, ano, autor_id)
            elif opcao == "2":
                livros = Livro.listar()
                for l in livros:
                    print(f"ID: {l[0]}, Título: {l[1]}, Ano: {l[2]}, Autor: {l[3]}")
            elif opcao == "3":
                id = input("ID do livro: ")
                titulo = input("Novo título: ")
                ano = input("Novo ano: ")
                autor_id = input("Novo ID do autor: ")
                Livro.atualizar(id, titulo, ano, autor_id)
            elif opcao == "4":
                id = input("ID do livro: ")
                Livro.excluir(id)
            elif opcao == "5":
                break
