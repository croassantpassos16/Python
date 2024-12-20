#Elabore um algoritmo que faça a leitura de dois números inteiros, x e y, e imprima o quociente
#e o resto da divisão inteira entre eles.

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))

if y == 0:
    print("DIVISÃO POR ZERO!!!!")

quociente = x / y
resto = x % y

print("O quociente da divisão dos dois números é", quociente, "e o resto é ", resto)
