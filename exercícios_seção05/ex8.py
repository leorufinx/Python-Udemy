nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

if nota1 < 0 or nota2 <0:
    print('nota inválida')

else:
    media = (nota1 + nota2)/2
    print('a média é:',media)

