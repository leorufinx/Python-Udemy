numero = int(input('Digite um número para comparar se é par ou impar: '))
resto = numero % 2

if resto is 0:
    print('o numero:', numero, 'é par')
else:
    print('o numero:', numero, 'é ímpar')
