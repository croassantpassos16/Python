'''Desenvolva um algoritmo que leia três número e 
informe qual é o maior entre eles.'''

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
z = float(input("Digite o terceiro número: "))

if x > y:
    if x > z:
        print("O primeiro valor é o maior de todos")
elif y > x:
    if y > z:
        print("O segundo valor é o maior de todos")
elif z > x:
    if z > y:
        print("O terceiro valor é o maior de todos")