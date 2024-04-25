anoCorrente = 2008

dia = 29
mes = 2
ano = 2000


if ano % 4 != 0:
    anoBissexto = False
elif ano % 100 != 0:
    anoBissexto = True
elif ano % 400 != 0:
    anoBissexto = False
else:
    anoBissexto = True


if ano == anoCorrente:
    if mes in (1, 3, 5, 7, 8, 10, 12):
        if dia > 0 and dia <= 31:
            pass
    elif mes == 2:
        if anoBissexto(ano):
            if dia > 0 and dia <= 29:
                pass
        else:
            if dia > 0 and dia <= 28:
                pass
    elif mes in (4, 6, 9, 11):
        if dia > 0 and dia <= 30:
            pass
    else:
        print("Data inválida")
        exit()
else:
    print("Data inválida")
    exit()


