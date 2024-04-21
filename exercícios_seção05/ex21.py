print('escolha a opção:')
print('1 - soma de 2 números')
print('2 - diferença entre 2 números')
print('3 - produte entre 2 números')
print('4 - divisão entre 2 números (o denominador não pode ser zero)')

opc = int(input('Digite sua opção:'))
n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))

match opc:
    case 1:
        res_soma = n1 + n2
        print('o resultado da soma é:',res_soma)
    case 2:
        if n1 > n2:
            res_sub = n1 - n2
            print('o resultado da subtração é:',res_sub)
        else:
            res_sub = n2 - n1
            print('o resultado da subtração é:',res_sub)
    case 3:
        res_mtp = n1 * n2
        print('o resultado da multiplicação é',res_mtp)
    case 4:
        if n2 !=0:
            res_div = n1/n2
            print('o resultado da divisão é:',res_div)
        else:
            print('o denominador deve ser maior que 0')
    case _:
        print('digite uma opção válida')
    