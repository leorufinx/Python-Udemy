"""faça um programa que leia um número e, caso ele seja positivo, calcule e mostre: *o número digitado ao quadrado e a raiz do número digitado"""

import math
numero = 145

if numero > 0: 
    res1 = numero * numero
    print(res1)
    res2 = math.sqrt(numero)
    print(res2)
else:
    print('numero inválido')
    
