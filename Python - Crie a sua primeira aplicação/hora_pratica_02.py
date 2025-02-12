
# Título do Arquivo de Atividades Práticas do Curso de "Python: Crrie a Sua Primeira Aplicação"
print('''

██╗░░██╗░█████╗░██████╗░░█████╗░  ██████╗░██████╗░░█████╗░████████╗██╗░█████╗░░█████╗░
██║░░██║██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗██╔══██╗
███████║██║░░██║██████╔╝███████║  ██████╔╝██████╔╝███████║░░░██║░░░██║██║░░╚═╝███████║
██╔══██║██║░░██║██╔══██╗██╔══██║  ██╔═══╝░██╔══██╗██╔══██║░░░██║░░░██║██║░░██╗██╔══██║
██║░░██║╚█████╔╝██║░░██║██║░░██║  ██║░░░░░██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░░██║
╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝
''')

# Função de Estilização
def negrito(texto):
    return f"\033[1m{texto}\033[0m"

# --------------------------------------

print(negrito('QUESTÃO 01'))
print('Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar')

print(negrito('\nRESPOSTA:'))

num_escolhido = int(input('Insira um número de sua preferência: '))
if (num_escolhido % 2 == 0):
    print(f'{num_escolhido} é par!')
else:
    print(f'{num_escolhido} é ímpar!')

# --------------------------------------

print(negrito('\nQUESTÃO 02'))
print('''
    Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo 
    com as seguintes condições:
    * Criança: 0 a 12 anos;
    * Adolescente: 13 a 18 anos;
    * Adulto: acima de 18 anos.''')

print(negrito('\nRESPOSTA:'))

idade_user = int(input('Digite a sua idade: '))

if (idade_user >= 0 and idade_user <= 12):
    print('Você é uma criança')

elif (idade_user >= 13 and idade_user <= 18):
    print('Você é um adolescente')

else:
    print('Você é um adulto')

# --------------------------------------

print(negrito('\nQUESTÃO 03'))
print('''
    Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos 
    correspondem aos valores esperados determinados por você.''')

print(negrito('\nRESPOSTA:'))

user_correto = 'Reh'
senha_correta = 'EuAmoTeteu<3'

tentativa_user = input('Digite o usuário: ')
tentativa_senha = input('Digite a senha: ')

if(tentativa_user == user_correto and tentativa_senha == senha_correta):
    print('O usuário e senha estão corretos!\nRealizando login...')
elif (tentativa_user == user_correto and tentativa_senha != senha_correta):
    print('O usuário está correto mas a senha está incorreta!\nTente novamente...')
elif(tentativa_user != user_correto and tentativa_senha == senha_correta):
    print('A senha está correto mas o usuário está incorreto!\nTente novamente...')
else:
    print('Nem o usuário nem a senha estão corretos!\nTente novamente...')
 
# --------------------------------------

print(negrito('\nQUESTÃO 04'))

print('''
   4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual 
   quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
    * Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    * Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    * Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    * Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    * Caso contrário: o ponto está localizado no eixo ou origem.
''')

print(negrito('\nRESPOSTA:'))

coord_x = int(input('Digite a coordenada de x: '))
coord_y = int(input('Digite a coordenada de y: '))

if(coord_x > 0 and coord_y > 0):
    print('O plano se encontra no Primeiro Quadrante do plano cartesiano')
elif(coord_x < 0 and coord_y > 0):
    print('O plano se encontra no Segundo Quadrante do plano cartesiano')
elif(coord_x < 0 and coord_y < 0):
    print('O plano se encontra no Terceiro Quadrante do plano cartesiano')
elif(coord_x > 0 and coord_y < 0):
    print('O plano se encontra no Quarto Quadrante do plano cartesiano')
else:
    print('O plano se encontra na origem ou no eixo do plano cartesiano')


# --------------------------------------
