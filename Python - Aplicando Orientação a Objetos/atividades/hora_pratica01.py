# Criando a classe
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

# ------------------------------------------

# Instanciando um objeto
restaurante_01 = Restaurante()
restaurante_01.nome = 'Praça'
restaurante_01.categoria = 'Praça' 
print(f'Nome: {restaurante_01.nome}\n Categoria: {restaurante_01.categoria}\n Status: {restaurante_01.ativo}\n')

# Altere o valor do atributo nome para 'Bistrô'.
restaurante_01.nome = 'Bistrô'
print(f'{restaurante_01.nome}')

# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_01.categoria = 'Italiana'

# Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_01.nome}\n Categoria: {restaurante_01.categoria}\n Status: {restaurante_01.ativo}\n')

# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
nome_restaurante_01 = restaurante_01.nome

# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
status_restaurante = restaurante_01.ativo
print(f'O restaurante {restaurante_01.nome} está ativo!') if status_restaurante == True else print(f'O restaurante {restaurante_01.nome} está inativo!')

# ------------------------------------------

# Criando um novo restaurante
restaurante_02 = Restaurante()
restaurante_02.nome = 'Pizza Place'
restaurante_02.categoria = 'Fast Food' 
print(f'Nome: {restaurante_02.nome}\n Categoria: {restaurante_02.categoria}\n Status: {restaurante_02.ativo}\n')

# ------------------------------------------

# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria

# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(f'A categoria do restaurante {restaurante_02.nome} é Fast Food!') if restaurante_02.categoria == 'Fast Food' else print(f'A categoria do restaurante {restaurante_02.nome} não é Fast Food!')

# Mude o estado da instância restaurante_pizza para ativo.
restaurante_02.ativo = True
print(f'Nome: {restaurante_02.nome}\n Categoria: {restaurante_02.categoria}\n Status: {restaurante_02.ativo}\n')
