#Desenvolva um programa no qual informe a área e o volume de um cilindro

import math

altura = float(input("Informe a altura do cilindro: "))
raio = float(input("Informe o raio do cilindro: "))

volume = (math.pi * math.pow(raio, 2) * altura)
area = ((2 * math.pi * raio) * (raio + altura))

volume = "{:.2f}".format(volume)
area = "{:.2f}".format(area)

print("O cilindro tem:", area, "de área e ", volume, "de volume")