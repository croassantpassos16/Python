'''Desenvolva um algoritmo que leia os três coeficientes de uma equação de 
segundo grau e determine suas raízes'''
import math

a = float(input("Digite o primeiro coeficiente: "))
b = float(input("Digite o segundo coeficiente: "))
c = float(input("Digite o terceiro coeficiente: "))

delta = ((math.pow(b, 2)) - 4 * a * c)

if delta < 0:
    print("ERRO: DELTA MENOR QUE ZERO!!")
else:
    raizdelta  =  math.sqrt(delta)
    x1 = (-b + raizdelta)/(2*a)
    x2 = (-b - raizdelta)/(2*a)
    print("As raízes são:", x1, "e", x2)



