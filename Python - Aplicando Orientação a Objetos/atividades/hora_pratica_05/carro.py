from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo, cor)
        self._portas = portas

    def __str__(self):
        return f'{super().__str__()} | Portas: {self._portas}'
    
    def ligar(self):
        self._ligado = True
        print(f'O  carro {self._modelo} está ligado')