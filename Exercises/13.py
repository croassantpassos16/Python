'''Sabendo que latão é constituído de 70% de cobre e 30% de zinco, 
crie um algoritmo que indique a quantidade de cada um desses componentes, 
em gramas, para se obter uma certa quantidade de
latão (requerida pelo usuário).
'''

latao = float(input("Digite a quantidade de latão: "))

cobre = latao * 0.7
zinco = latao * 0.3

print("Para fazer ", latao, "de latão, será necessário:", cobre, "de cobre e", zinco, "de zinco.")
