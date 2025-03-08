from hora_pratica_04 import Livro

# Instanciando a classe livro
livro01 = Livro('Príncipe Cruel', 'Holly Black', 2018)
livro02 = Livro('Rei Perverso', 'Holly Black', 2020)
livro03 = Livro('Rainha do Nada', 'Holly Black', 2020)

# Lista de livros
Livro.livros = [livro01, livro02, livro03]
livro01.emprestar()

print(livro01)
print(livro02)
print(livro03)

def __str__(self):
    return f'{self.livros_disponiveis_ano}'

ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")