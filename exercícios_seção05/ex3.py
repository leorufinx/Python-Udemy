""" leia um numero real. se for positivo, imprima a raiz quadrada. do contrário imprima o número ao quadrado """

import math
numero = -10

if numero > 0:
   res1 = math.sqrt(numero)
   print(res1)
else:
   res2 = numero * numero
   print(res2)