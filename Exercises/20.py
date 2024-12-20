'''Elabore um algoritmo que avaliando um determinado valor fornecido pelo usuário informe
se um dado ano é ou não bissexto. Informe o critério adotado.
'''

ano = int(input("Digite o ano desejado: "))

if ano % 4 == 0:
    if ano % 100 != 0:
        print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")