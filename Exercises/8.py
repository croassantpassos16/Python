'''Crie um algoritmo que leia a razão de uma PA (Progressão Aritmética), o seu primeiro e
último termos e informe a soma de todos os elementos dessa PA.'''

x1 = float(input("Digite o primeiro termo: "))
xn = float(input("Digite o último termo: "))
rn = float(input("Digite a razão da PA: "))

qnt = -((x1 - xn - rn) / (rn))

print("A PA possui", qnt, "termos")

soma = (((x1 + xn) * qnt)/(2))

print("A soma de todos os termos da PA é", soma)