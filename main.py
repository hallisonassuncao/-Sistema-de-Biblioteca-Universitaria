from view.menu_principal import MenuPrincipal
from controller.autor_controller import AutorController
from controller.livro_controller import LivroController

def main():
    while True:
        MenuPrincipal.menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            AutorController.gerenciar()
        elif opcao == "2":
            LivroController.gerenciar()
        elif opcao == "3":
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
