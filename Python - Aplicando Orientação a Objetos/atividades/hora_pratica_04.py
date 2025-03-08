#1. Crie uma classe chamada Livro com um construtor que aceita osparâmetros titulo, autor e ano_publicacao. Inicie um atributochamado disponivel como True por padrão.
#2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
#3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
#4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma listados livros disponíveis publicados nesse ano.

# Criação da Classe
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    # Método Especial
    def __str__(self):
        return f'{self._titulo.ljust(15)} | {self._autor.ljust(15)} | {str(self._ano_publicacao).ljust(8)} | {self._disponivel}'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis
    
