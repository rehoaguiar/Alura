# Importando Bibliotecas
import os
import time

# Criando uma lista de restaurantes
restaurantes = [
    {'nome':'Le Touchè','categoria':'francesa','ativo': False},
    {'nome':'Always','categoria':'brasileira','ativo': True},
    {'nome':'Forever','categoria':'americana','ativo': True}
]

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

def montar_cabecalho(texto):
    limpar_tela()
    exibir_nome_app()
    print(texto)

# Opções do aplicativo
def exibir_menu():
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Status do Restaurante')
    print('4. Sair')

def finalizar_app():
    
    for ii in range(15, 0, -1):
        print(f'O aplicativo será finalizado em {ii} segundos\n', end='', flush=True)
        time.sleep(1)

        limpar_tela()
   
def main():
    limpar_tela()
    exibir_nome_app()
    exibir_menu()
    escolher_opcao()

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('\nOpção inválida')
    voltar_menu()

def cadastrar_restaurante():
    montar_cabecalho('''
    █▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
    █▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█''')    
    
    nome_restaurante = input('\n\nDigite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')

    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)

    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')

    voltar_menu()

def listar_restaurante():
    montar_cabecalho('''
    █░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
    █▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█\n''')

    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_menu()

def alterar_status():
    montar_cabecalho('''
    ▄▀█ █░░ ▀█▀ █▀▀ █▀█ ▄▀█ █▀█   █▀ ▀█▀ ▄▀█ ▀█▀ █░█ █▀   █▀▄ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
    █▀█ █▄▄ ░█░ ██▄ █▀▄ █▀█ █▀▄   ▄█ ░█░ █▀█ ░█░ █▄█ ▄█   █▄▀ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄''')


    nome_restaurante = input('\nDigite o nome do restaurante que deseja alterar o status: ').strip()
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
            
    if not restaurante_encontrado:
        print(f'\nO restaurante {nome_restaurante} não foi encontrado')
        
    voltar_menu()

def escolher_opcao():
    # Definindo variáveos
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        match(opcao_escolhida):
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()
            case 3: 
                alterar_status()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

if __name__ == '__main__':
    main()