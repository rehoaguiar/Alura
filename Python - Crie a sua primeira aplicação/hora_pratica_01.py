
# Título do Arquivo de Atividades Práticas do Curso de "Python: Crrie a Sua Primeira Aplicação"
print('''

██╗░░██╗░█████╗░██████╗░░█████╗░  ██████╗░██████╗░░█████╗░████████╗██╗░█████╗░░█████╗░
██║░░██║██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗██╔══██╗
███████║██║░░██║██████╔╝███████║  ██████╔╝██████╔╝███████║░░░██║░░░██║██║░░╚═╝███████║
██╔══██║██║░░██║██╔══██╗██╔══██║  ██╔═══╝░██╔══██╗██╔══██║░░░██║░░░██║██║░░██╗██╔══██║
██║░░██║╚█████╔╝██║░░██║██║░░██║  ██║░░░░░██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░░██║
╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝
''')

# 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵 𝗤𝗨𝗘𝗦𝗧𝗜𝗢𝗡 𝗔𝗡𝗦𝗪𝗘𝗥

# Função de Estilização
def negrito(texto):
    return f"\033[1m{texto}\033[0m"

# --------------------------------------

print(negrito('QUESTÃO 01'))
print('Imprima a frase: Python na Escola de Programação da Alura')

print(negrito('\nRESPOSTA:'))
print('Python na Escola de Programação da Alura')

# --------------------------------------

# Questão 02 e sua respectiva resposta
print(negrito('\nQUESTÃO 02'))
print('Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis')

# Declarando as variáveis que recebem um input
nome = input('\nDigite o seu nome: ')
idade = int(input('Digite a sua idade: '))

print(negrito('\nRESPOSTA:'))
print(f'Meu nome é {nome} e tenho {idade} anos')

# --------------------------------------

print(negrito('\nQUESTÃO 03'))
print('Imprima a palavra: ALURA de modo que cada letra fique em uma linha')

print(negrito('\nRESPOSTA:'))

print('\nA\nL\nU\nR\nA')

# --------------------------------------

# Questão 04 e sua respectiva resposta
print(negrito('\nQUESTÃO 04'))

print('''
    Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para 
    apenas duas casas decimais. Para facilitar, utilize: pi = 3.14159
''')

# Declarando o valor de pi
pi_arredondado = round(3.14159, 2)

print(negrito('\nRESPOSTA:'))
print(f'O valor arredondado de pi é: {pi_arredondado}')

# --------------------------------------