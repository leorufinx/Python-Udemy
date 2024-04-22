opc = int(input('digite o código do produto desejado: '))
qtd = int(input('digite a quantidade desejada: '))

match opc:
    case 100:
        res = qtd * 1.20
        print('voce terá que pagar: R$',res)

    case 101:
        res = qtd * 1.30
        print('voce terá que pagar: R$',res)

    case 102:
        res = qtd * 1.50
        print('voce terá que pagar: R$',res)

    case 103:
        res = qtd * 1.20
        print('voce terá que pagar: R$',res)

    case 104:
        res = qtd * 1.70
        print('voce terá que pagar: R$',res)

    case 105:
        res = qtd * 2.20
        print('voce terá que pagar: R$',res)

    case 106:
        res = qtd * 1.00
        print('voce terá que pagar: R$',res)

    case _:
        print('digite um valor válido')