'''Elabore um algoritmo que gere o preço de compra de um veículo e os 
valores pagos em imposto, bem como o lucro do distribuidor. 
Sabe-se: o custo de fábrica do veículo a taxa de imposto em
45% sobre o custo do carro e o lucro do distribuidor sendo 12% sobre o 
custo do carro.
'''
nomecarro = input("Digite o nome do carro: ")
precofabrica = float(input("Entre com o preço de fábrica: "))

imposto = precofabrica * 0.45
lucrodistribuidor = precofabrica * 0.12

precocompra = precofabrica + lucrodistribuidor + imposto

print("O", nomecarro, "custa", precocompra, "sendo incluso", imposto, "de imposto e", lucrodistribuidor, "de lucro ao distribuidor")

