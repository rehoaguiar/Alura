# rie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa():
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade} | Profissão: {self._profissao}'
    
    def aniversario(self):
        self._idade += 1
    
    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}! Trabalho como {self._profissao}'
        else:
            return f'Olá! Sou {self._nome}'
    
pessoa1 = Pessoa('Reh', 20,'Programadora')
print(pessoa1)

pessoa1.aniversario()
print(pessoa1)

print(pessoa1.saudacao)