#Atividade 05 Consumo de energia
nome = input("Olá  Caro  Cliente,por favor digite seu nome:")
nome_eletro = input("Qual seria o aparelho que você queira saber o consumo:")
potencia = float(input("Quantos Watts tem o aparelho:"))
HorasDia = float(input("Quantos horas voce usa o aparelho:"))
Consumo_mês = (potencia * HorasDia * 30) / 1000
Preço_final = ( Consumo_mês * 0.75)
print ("____________________________")
print (f"seu aparelho = {nome_eletro}")
print (f" seu consumo mensal foi = {Consumo_mês:.2f} ")
print (f"preço final: R${Preço_final:.2f}")

