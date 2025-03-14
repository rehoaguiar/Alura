from veiculo import Veiculo
from carro import Carro
from moto import Moto

carro_01 = Carro('Honda', 'Civic', 4, 'Preto')
carro_02 = Carro('Lamborghini', 'Huracán', 2, 'Rosa')
carro_03 = Carro('Hyundai', 'Veloster', 3, 'Vemelho')

moto_01 = Moto('Yamaha ', 'YZF-R1', 'Esportiva', 'Preta')
moto_02 = Moto('Honda', 'CB 500F', 'Casual', 'Rosa')
moto_03 = Moto('Ducati ', 'Panigale V4', 'Esportiva', 'Roxa')

carro_01.ligar()

lista_veiculos = [carro_01, carro_02, carro_03, moto_01, moto_02, moto_03]

for item in lista_veiculos:
    print(item)