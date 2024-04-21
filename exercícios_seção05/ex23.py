ano = int(input('digite um ano para ver se é bissexto: '))

if ano%4 == 0 or ano%400 == 0 and ano%100 !=0 :
    print(ano,'é um ano bissexto')
else:
    print(ano, 'é ano comum')
