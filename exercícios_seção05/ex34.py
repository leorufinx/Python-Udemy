nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Digite a quantidade de faltas cometitas por um aluno: '))

if nota >= 9.0 and nota <=10 and faltas <= 20:
    print('A')

else:
    if nota >= 9.0 and nota <=10 and faltas > 20:
        print('B')

    elif nota >= 7.5 and nota <= 8.9 and faltas <=20:
        print('B')

    elif nota >= 7.5 and nota <= 8.9 and faltas > 20:
        print('C')

    elif nota >= 5.0 and nota <= 7.4 and faltas <= 20:
        print('C')

    elif nota >= 5.0 and nota <= 7.4 and faltas > 20:
        print('D')

    elif nota >= 4.0 and nota <= 4.9 and faltas <= 20:
        print('D')

    elif nota >= 4.0 and nota <= 4.9 and faltas > 20:
        print('E')

    elif nota >= 0.0 and nota <= 3.9 and faltas <= 20:
        print('E')

    else:
        print('E')