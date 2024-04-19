base1 = float(input('digite o valor da primeira base: '))
base2 = float(input('digite o valor da segunda base: '))
altura = float(input('digite o valor da altura: '))

if base1 <0 or base2 <0:
    print('digite numeros válidos')

else:
    area = (base1 + base2) * altura /2
    print('a area do trapézio é:',area)