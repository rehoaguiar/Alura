# Importando Bibliotecas
import os
import time

# Definindo Funções
# Apresentação do nome do restaurante
def exibir_titulo():
    print('''
    ███████╗░█████╗░░██████╗████████╗  ██████╗░██╗███████╗████████╗
    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝  ██╔══██╗██║██╔════╝╚══██╔══╝
    █████╗░░███████║╚█████╗░░░░██║░░░  ██║░░██║██║█████╗░░░░░██║░░░
    ██╔══╝░░██╔══██║░╚═══██╗░░░██║░░░  ██║░░██║██║██╔══╝░░░░░██║░░░
    ██║░░░░░██║░░██║██████╔╝░░░██║░░░  ██████╔╝██║███████╗░░░██║░░░
    ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝╚══════╝░░░╚═╝░░░
    ''')

# Opções do aplicativo
def exibir_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def finalizar_app():
    
    for ii in range(16,1):
        print(f'O aplicativo será finalizado em {ii} segundos\n', end='', flush=True)
        time.sleep(1)

    os.system('cls')
    # os.system('clear') # No Sistema MAC utilizamos o comando clear

def escolher_opcao():
    # Definindo variáveos
    opcao_escolhida = int(input('\nEscolha uma opção: '))

    if (opcao_escolhida == 1):
        print('Cadastrar Restaurante')

    elif (opcao_escolhida == 2):
        print('Listar Restaurante')

    elif (opcao_escolhida == 3):
        print('Ativar Restaurante')

    else:
        finalizar_app()


def main():
    exibir_titulo()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()