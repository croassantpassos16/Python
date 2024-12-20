'''Permita com que um usuário indique 2 números inteiros no teclado e 
no caso do segundo ser diferente de zero, calcular e 
imprimir o quociente do primeiro pelo segundo. 
Caso contrário, imprimir a seguinte mensagem: ERRO: DIVISÃO POR ZERO'''

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

if y != 0:
    quo = x / y
    print("O quociente da divisão é", quo)
else:
    print("ERRO: DIVISÃO POR ZERO")
