'''Desenvolva um algoritmo que leia 2 números inteiros do teclado (A e B) e 
verifique imprimindo na tela qual deles é o maior, ou a mensagem “A = B”, 
caso sejam iguais'''

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a > b:
    print("A é maior que B")
elif a < b:
    print("A é menor que B")
else:
    print("A é igual a B")
    