TrabalhoLaboratorio = float(input('digite a nota do trabalho de laboratório: '))
AvaliacaoSemestra = float(input('digite a nota da avaliação semestral: '))
ExameFinal = float(input('digite a nota do exame final: '))

nota1_att = TrabalhoLaboratorio * 2
nota2_att = AvaliacaoSemestra * 3
nota3_att = ExameFinal * 5

media = (nota1_att + nota2_att + nota3_att)/10

if media < 0:
    print('erro: digite um valor válido')

elif media <= 2.9 :
    print('O aluno está reprovado')
    print('A média do aluno foi:',media)

elif media <= 4.9 :
    print('O aluno está de recuperação')
    print('A média do aluno foi:',media)

elif media >= 5:
    print('O aluno está aprovado!')
    print('A média do aluno foi:',media)



