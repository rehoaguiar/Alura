from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Place', 'Fast Food')

restaurante_praca.receber_avaliacao('Reh', 3)
restaurante_praca.receber_avaliacao('Teteu', 2)
restaurante_praca.receber_avaliacao('May', 5)

restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
