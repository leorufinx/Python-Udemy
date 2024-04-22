dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if mes == 2 and (ano % 4 == 0 or ano % 400 == 0) and ano % 100 != 0 and dia > 29:
    print('Data inválida')

else:
    if mes == 2 and dia > 28:
        print('data inválida')
  
    elif mes == 1 and dia < 32:
        print('data válida')
    
    elif mes == 3 and dia < 32:
        print('data válida')

    elif mes == 4 and dia < 31:
        print('data válida')

    elif mes == 5 and dia < 32:
        print('data válida')

    elif mes == 6 and dia < 31:
        print('data válida')

    elif mes == 7 and dia < 32:
        print('data válida') 

    elif mes == 8 and dia < 32:
        print('data válida')

    elif mes == 9 and dia < 31:
        print('data válida')

    elif mes == 10 and dia < 32:
        print('data válida')

    elif mes == 11 and dia < 31:
        print('data válida')

    elif mes == 12 and dia < 32:
        print('data válida')


""" dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

# Verificar se o mês está dentro do intervalo válido (de 1 a 12)
if mes < 1 or mes > 12:
    print('Data inválida')
else:
    # Lista com o número máximo de dias para cada mês
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar se o ano é bissexto e ajustar o número de dias de fevereiro se necessário
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        dias_por_mes[1] = 29

    # Verificar se o dia está dentro do intervalo válido para o mês fornecido
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        print('Data inválida')
    else:
        print('Data válida')
"""
