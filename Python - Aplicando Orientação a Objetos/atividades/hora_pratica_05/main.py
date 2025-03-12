from veiculo import Veiculo
from carro import Carro
from moto import Moto


carro_01 = Carro('Honda', 'Civic', 4)
carro_02 = Carro('Lamborghini', 'Huracán', 2)
carro_03 = Carro('Hyundai', 'Veloster', 3)

moto_01 = Moto('Yamaha ', 'YZF-R1', 'Esportiva')
moto_02 = Moto('Honda', 'CB 500F', 'Casual')
moto_03 = Moto('Ducati ', 'Panigale V4', 'Esportiva ')

lista_veiculos = [carro_01, carro_02, carro_03, moto_01, moto_02, moto_03]

for item in lista_veiculos:
    print(item)