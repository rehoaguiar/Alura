# Criando a classe
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

# Criando dois novos restaurantes
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Praça' 

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food' 

restaurantes = [restaurante_praca, restaurante_pizza]

for restaurante in restaurantes:
    print(vars(restaurante))