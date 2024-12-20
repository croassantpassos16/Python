'''Construa um algoritmo que realize a leitura de dois valores reais do teclado, calcule e imprima:
a) A soma destes valores 
b) O produto deles 
c) O quociente entre eles.
'''

x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))

if y == 0:
    print("DIVISÃO POR ZERO!!!")

soma = x + y
produto = x * y
quociente = x / y

print("Soma:", soma)
print("Produto:", produto)
print("Quociente:", quociente)

