#Construa um algoritmo para efetuar o cálculo da média final usando ponderação de três
#avaliações. Ou seja, dadas as notas de 3 provas P1, P2 e P3 com pesos 0,5, 0,3 e 0,2, respectivamente,
#produzir uma saída com a média final, bem como a situação do aluno de acordo com o seguinte critério:
#Mfinal ≥ 7, aprovado; 5 ≤ Mfinal ≤ 7, recuperação; Mfinal ≤ 5, reprovado.

test1 = float(input("Digite a nota da primeira avaliação:"))
test2 = float(input("Digite a nota da segunda avaliação:"))
test3 = float(input("Digite a nota da terceira avaliação:"))

media1 = ((test1 * 0.5) + (test2 * 0.3) + (test3 * 0.2)) / (1)

media = "{:.2f}".format(media1)

print("A média final é:", media)

if media1 >= 7:
    print("O aluno está aprovado")
elif 7 < media1 and media1 <= 5:
    print("O aluno está de recuperação")
elif media1 < 5:
    print("O aluno está reprovado")
else:
    print("Erro identificado")
