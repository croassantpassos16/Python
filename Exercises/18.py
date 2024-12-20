'''Elabore um algoritmo para a geometria plana no qual irá ler três valores 
e informará ao usuário se eles formam um triângulo. 
Caso afirmativo, dizer seu tipo (equilátero, isósceles ou escaleno).
'''

a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

if a == b and b == c:
    print("O triângulo é equilátero")
elif a == b or b == c or c == a:
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")
