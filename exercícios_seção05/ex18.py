print('ESCOLHA UMA OPERAÇÃO')
print('* para multiplicação')
print('+ para soma')
print('- para subtração')
print('% para divisão')

opr = input('digite a operação desejada: ')

if opr == '*':
    print('Você escolheu multiplicação')
    n1_mtp = float(input('digite o primeiro número: '))
    n2_mtp = float(input('digite o segundo número: '))
    res_mtp = n1_mtp * n2_mtp
    print('o resultado da multiplicação é: ',res_mtp)

elif opr == '+':
    print('Você escolheu soma')
    n1_soma = float(input('digite o primeiro número: '))
    n2_soma = float(input('digite o segundo número: '))
    res_soma = n1_soma + n2_soma
    print('o resultado da soma é de: ',res_soma)

elif opr == '-':
    print('Você escolheu subtração')
    positivoNegativo = (input('se deseja uma subtração positiva digite "P", caso aceite a possibilidade de subtração negativa, digite "N": '))
    if positivoNegativo == 'P' or positivoNegativo == 'p':
        n1_sub = float(input('digite o primeiro número: '))
        n2_sub = float(input('digite o segundo número: '))
        if n1_sub > n2_sub:
            res_sub = n1_sub - n2_sub
            print('o resultado da sua subtração positiva é: ',res_sub)
        else:
            res_sub = n2_sub - n1_sub
            print('o resultado da sua subtração positiva é: ',res_sub)
    elif positivoNegativo == 'N' or positivoNegativo == 'n':
        n1_sub = float(input('digite o primeiro número: '))
        n2_sub = float(input('digite o segundo número: '))
        res_sub = n1_sub - n2_sub
        print('o resultado da sua subtração é: ',res_sub)
    else:
        print('digite um valor válido')

elif opr == '%':
    print('Você escolheu divisão')
    n1_div = float(input('digite o primeiro número: '))
    n2_div = float(input('digite o segundo número: '))
    res_div = n1_div/n2_div
    print('o resultado da divisão é:',res_div)
