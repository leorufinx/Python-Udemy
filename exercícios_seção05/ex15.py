dia = int(input('digite um numero entre 1 e 7: '))

match dia:
    case 1:
        print('segunda-feira')
    case 2:
        print('terca-feira')
    case 3:
        print('quarta-feira')
    case 4:
        print('quinta-feira')
    case 5:
        print('sexta-feira')
    case 6:
        print('sabado')
    case 7:
        print('domingo')
    case _:
        print('erro: digite um dia válido')
    