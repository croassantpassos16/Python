'''Desenvolva um programa que calcule os valores de multas de trânsito por 
excesso de velocidade. O algoritmo deverá ler: a velocidade máxima 
permitida em uma avenida e a velocidade com que o
motorista estava dirigindo nela. Sabe-se que os valores das multas são: 
a) 50 reais se o motorista ultrapassarem até 10km/h a velocidade permitida; 
b) 100 reais, se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida. 
c) 200 reais, se estiver acima de 31km/h da velocidade permitida.'''

vmax = int(input("Digite a velocidade máxima da avenida: "))
vmot = int(input("Digite a velocidade que o motorista estava dirigindo: "))

diferenca = vmot - vmax

if diferenca <= 0:
    print("O motorista não excedeu o limite de velocidade")
elif diferenca <= 10 and diferenca > 0:
    print("A multa será de 50 reais")
elif diferenca <= 30 and diferenca >= 11:
    print("A multa será de 100 reais")
elif diferenca > 30:
    print("A multa será de 200 reais")
