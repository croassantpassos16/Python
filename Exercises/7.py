'''Elabore um programa que leia 3 números reais do teclado 
verificando se o primeiro é maior que a soma dos outros dois. 
Imprima na tela apresentando os número e informando a condição.
'''

x = float(input("Digite o primeiro valor:"))
y = float(input("Digite o segundo valor:"))
z = float(input("Digite o terceiro valor:"))

yz = y + z

print("A soma de", y, "e", z, "é", yz)

if yz > x: 
   print("Portanto, a soma é maior que o primeiro valor")
elif yz < x:
   print("Portanto, a soma é menor que o primeiro valor")
else:
   print("Portanto, a soma é igual que o primeiro valor")