salarioAtual = float(input('Digite o valor do seu salário atual: '))
anosTrabalhados = int(input('Digite o tempo de serviço que possui na empresa: '))

if salarioAtual <= 500:
    salarioReajustado = salarioAtual + salarioAtual * 0.25

else:
    if salarioAtual > 500 and salarioAtual <= 1000:
        salarioReajustado = salarioAtual + salarioAtual * 0.20
    
    elif salarioAtual > 1000 and salarioAtual <= 1500:
        salarioReajustado = salarioAtual + salarioAtual * 0.15
    
    elif salarioAtual > 1500 and salarioAtual <= 2000:
        salarioReajustado = salarioAtual + salarioAtual * 0.10
    
    else:
        salarioReajustado = salarioAtual


if anosTrabalhados < 1:
    print(salarioReajustado)

else:
    if anosTrabalhados >= 1 and anosTrabalhados <= 3:
        salarioComBonus = salarioReajustado + 100
        print(salarioComBonus)

    elif anosTrabalhados >= 4 and anosTrabalhados <= 6:
        salarioComBonus = salarioReajustado + 200
        print(salarioComBonus)

    elif anosTrabalhados >= 7 and anosTrabalhados <= 10:
        salarioComBonus = salarioReajustado + 300
        print(salarioComBonus)

    else:
        salarioComBonus = salarioReajustado + 500
        print(salarioComBonus)