# faça um programa que leia duas notas de um aluno, verifique se as notas são válidas e exiba na tela a média dessas notas. uma nota válida
# deve ser, obrigatóriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido esse fato deve ser informado ao usuário 
# e o programa termina.

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

if nota1 < 0 or nota2 <0:
    print('nota inválida')

else:
    media = (nota1 + nota2)/2
    print('a média é:',media)

