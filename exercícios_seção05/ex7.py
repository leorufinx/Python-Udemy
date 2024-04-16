# faça um programa que receba dois números e mostre o maior. se por acaso, os dois numeros forem iguais, imprima a mensagem 'numeros iguais'

numero1 = int(input('digite um numero: '))
numero2 = int(input('digite outro numero: '))

if numero1 > numero2:
    print('numero maior: ', numero1)
elif numero2 > numero1:
    print('numero maior:', numero2)
elif numero1 == numero2:
    print('numeros iguais')