from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo, cor):
        super().__init__(marca, modelo, cor)
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()} | Tipo de Moto: {self._tipo}'
    
    def ligar(self):
        self._ligado = True
        print(f'A moto {self._modelo} está ligada')