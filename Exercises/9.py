'''Por meio da programação desenvolva um algoritmo que efetue a leitura de um nome no teclado
e avalie se é igual ao seu nome. Imprimir o resultado: “NOME CORRETO” ou “NOME INCORRETO”.
'''
nome = input("Digite o nome de entrada: ")

if nome.casefold() == "matheus":
    print("Nome correto")
else:
    print("Nome incorreto")
