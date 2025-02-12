# Importando Bibliotecas
import os
import time

# Criando uma lista de restaurantes
restaurantes = []

# Definindo Funções
# Apresentação do nome do restaurante
def exibir_nome_app():
    print('''
    ███████╗░█████╗░░██████╗████████╗  ██████╗░██╗███████╗████████╗
    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝  ██╔══██╗██║██╔════╝╚══██╔══╝
    █████╗░░███████║╚█████╗░░░░██║░░░  ██║░░██║██║█████╗░░░░░██║░░░
    ██╔══╝░░██╔══██║░╚═══██╗░░░██║░░░  ██║░░██║██║██╔══╝░░░░░██║░░░
    ██║░░░░░██║░░██║██████╔╝░░░██║░░░  ██████╔╝██║███████╗░░░██║░░░
    ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝╚══════╝░░░╚═╝░░░''')

def limpar_tela():
    os.system('cls')
    # os.system('clear') # No Sistema MAC utilizamos o comando clear

# Opções do aplicativo
def exibir_menu():
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def finalizar_app():
    
    for ii in range(16,1):
        print(f'O aplicativo será finalizado em {ii} segundos\n', end='', flush=True)
        time.sleep(1)

        limpar_tela()
   
def main():
    limpar_tela()
    exibir_nome_app()
    exibir_menu()
    escolher_opcao()

def opcao_invalida():
    print('\nOpção inválida')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_restaurante():
    limpar_tela()
    exibir_nome_app()

    print('''
    █▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
    █▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█''')    
    
    nome_do_restaurante = input('\n\nDigite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():
    # Definindo variáveos
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        match(opcao_escolhida):
            case 1:
                cadastrar_restaurante()
            case 2:
                print('Listar Restaurante')
            case 3: 
                print('Ativar Restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

if __name__ == '__main__':
    main()