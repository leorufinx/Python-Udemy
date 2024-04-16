""" leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. se for negativo,
 mostre uma mensagem dizendo que o número é inválido """

import math
numero = 9

if numero > 0:
   res =  math.sqrt(numero)
   print(res)
else:
   print('Número inválido')


