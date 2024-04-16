# escreva um programa que, dado dois números inteiros, mostre na tela o maior, assim como a diferença entre eles

numero1 = int(input('digite um número: '))
numero2 = int(input('digite outro número: '))



if numero1 > numero2:
    res1 = numero1 - numero2
    print(numero1, 'é maior que', numero2, 'e a diferença entre eles é de:', res1)

elif numero2 > numero1:
    res2 = numero2 - numero1
    print(numero2, 'é maior que', numero1, 'e a diferença entre eles é de:', res2)

elif numero1 == numero2:
    print('numeros iguais, não há diferença')

