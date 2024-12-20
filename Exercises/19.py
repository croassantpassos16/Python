'''Execute a leitura de 4 números inteiros, por meio de um algoritmo, e 
calcule a soma apenas daqueles números que forem par.
'''

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
d = int(input("Digite o quarto número: "))

par =[]
num = [a, b, c, d]

for n in num:
    if n % 2 == 0:
        par.append(n)    

print("A soma dos pares é:", sum(par))


