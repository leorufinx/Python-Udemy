idade = int(input('digite a sua idade: '))
tempo_trabalhado = int(input('digite o tempo de serviço: '))

if idade >= 60 and tempo_trabalhado >= 25:
    print('Pode se aposentar!')

elif tempo_trabalhado >= 30:
    print('Pode se aposentar!')

elif idade >= 65:
    print('Pode se aposentar!')

else:
    print('Não pode se aposentar')

