'''Desenvolva um algoritmo que leia três número e 
imprima-os em ordem crescente.'''

x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))
z = float(input("Digite o terceiro valor: "))

if x > y:
    if y > z:
        print("A sequência é:", x, y, z)
    elif y < z:
        print("A sequência é:", x, z, y)
    else:
        print("O", y, "e", z, "são iguais")
elif y > x:
    if x > z:
        print("A sequência é: ", y, x, z)
    elif x < z:
        print("A sequência é", y, z, x)
    else:
        print("O", x, "e", z, "são iguais")
elif z > x:
    if x > y:
        print("A sequência é:", z, x, y)
    elif x < y:
        print("A sequência é:", z, y, x)
    else:
        print("O", x, "e", y, "são iguais")
else:
    print("Todos os números são iguais")