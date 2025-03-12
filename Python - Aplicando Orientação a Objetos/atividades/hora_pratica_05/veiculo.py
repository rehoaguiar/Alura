class Veiculo():
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Estado: {status}'