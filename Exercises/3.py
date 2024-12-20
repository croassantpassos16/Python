#Desenvolva o cálculo da quantidade de dinheiro gasto por um fumante por meio de programação. 
#Utilize como dados os seguintes parâmetros: o número de anos que ele fuma
#no de cigarros fumados por dia e o preço de uma carteira de cigarros.

qntCigarro = int(input("Quantos cigarros vc fuma por dia: "))
anos = int(input("Há quantos anos vc fuma: "))

cigarroTotal = qntCigarro * (anos*365)
gasto = cigarroTotal*13.99

gasto = "{:.2f}".format(gasto)

print("Em", anos, "anos, o fumante gastou R$", gasto)