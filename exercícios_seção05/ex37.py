# Entrada dos horários de chegada e saída em horas e minutos
hora_chegada = int(input("Digite a hora de chegada: "))
minuto_chegada = int(input("Digite o minuto de chegada: "))
hora_saida = int(input("Digite a hora de saída: "))
minuto_saida = int(input("Digite o minuto de saída: "))

# Conversão dos horários de chegada e saída para minutos
minutos_chegada = hora_chegada * 60 + minuto_chegada
minutos_saida = hora_saida * 60 + minuto_saida

# Cálculo do total de minutos estacionados
total_minutos = (minutos_saida - minutos_chegada) % (24 * 60)

# Cálculo do total de horas estacionadas, arredondando para cima até a hora mais próxima
total_horas = -(-total_minutos // 60)

# Cálculo da taxa de estacionamento
if total_horas <= 2:
    taxa = total_horas * 1.00
elif total_horas <= 4:
    taxa = 2 * 1.00 + (total_horas - 2) * 1.40
else:
    taxa = 2 * 1.00 + 2 * 1.40 + (total_horas - 4) * 2.00

# Impressão da taxa de estacionamento
print("Taxa de estacionamento: R$ {:.2f}".format(taxa))