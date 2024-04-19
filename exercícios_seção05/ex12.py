import math
numero = int(input('digite um número:'))

if numero > 0:
    log = math.log(numero)
    print('O log de',numero, 'é', log)

else:
    print('digite um número válido')

