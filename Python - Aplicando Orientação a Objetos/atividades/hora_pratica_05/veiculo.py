from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, cor):
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._ligado = False

    def __str__(self):
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Estado: {status}'
    
    @abstractmethod
    def ligar(self):
        pass