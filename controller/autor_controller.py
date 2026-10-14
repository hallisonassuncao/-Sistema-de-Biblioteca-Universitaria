from model.autor import Autor
from view.autor_view import AutorView

class AutorController:
    @staticmethod
    def gerenciar():
        while True:
            AutorView.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                nome = input("Nome: ")
                nacionalidade = input("Nacionalidade: ")
                Autor.cadastrar(nome, nacionalidade)
            elif opcao == "2":
                autores = Autor.listar()
                for a in autores:
                    print(f"ID: {a[0]}, Nome: {a[1]}, Nacionalidade: {a[2]}")
            elif opcao == "3":
                id = input("ID do autor: ")
                nome = input("Novo nome: ")
                nacionalidade = input("Nova nacionalidade: ")
                Autor.atualizar(id, nome, nacionalidade)
            elif opcao == "4":
                id = input("ID do autor: ")
                Autor.excluir(id)
            elif opcao == "5":
                break
