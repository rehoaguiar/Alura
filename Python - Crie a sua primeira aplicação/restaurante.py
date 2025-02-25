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
    ''' Exibe o nome do programa, a fonte foi encontrada no site fsymbols '''
    
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
    ''' Limpa a tela, exibe o nome do aplicativo e, por fim, recebendo o input texto, ele exibe o texto recebido na tela '''
    
    limpar_tela()
    exibir_nome_app()
    print(texto)

# Opções do aplicativo
def exibir_menu():
    ''' Mostra todas as 4 opções do menu, sendo elas: Cadastrar Restaurante; Listar Restaurantes; Alterar Status do Restaurante; Sair do aplicativo '''
    
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Status do Restaurante')
    print('4. Sair')

def finalizar_app():
    ''' Inicia uma contagem regressiva de 15 segundos e limpa o prompt de comando, encerrando, então, o aplicativo '''

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
    ''' Exibe opção inválida na tela e chama a função voltar ao menu '''
    
    print('\nOpção inválida')
    voltar_menu()

def cadastrar_restaurante():
    ''' Exibe o nome da funcionalidade na tela e recebe o input do nome do restaurante a ser cadastrado. Em seguida, recebe também o nome da categoria e cria um dicionário com essas informações. Por fim, ele confirma ao usuário que o restaurante em questão foi cadastrado e volta para o menu '''
    
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
    ''' Exibe o nome da funcionalidade na tela e exibe o subtítulo (Nome do restaurante; Categoria; Status) seguido das informações dos restaurantes contidas em cada um deles. A função utiliza a estrutura de repetição for para listar cada um dos restaurantes '''
    
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
    ''' Exibe o nome da funcionalidade na tela e recebe um imput com o nome do restaurante. Ele utiliza de uma estrutura de repetição for para ativar e desativar o restaurante digitado pelo usuário. Caso ele não tenha sido encontrado ele apresentará uma mensagem de erro '''
    
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
    ''' Ele pede para o usuário digitar o número da funcionalidade que ele deseja utilizar no código. Em caso de erro ele sinaliza que a opção é inválida '''
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