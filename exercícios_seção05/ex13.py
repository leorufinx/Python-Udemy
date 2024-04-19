nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))

if nota1 <0 or nota2 <0 or nota3 <0:
    print('Erro: digite numeros válidos')

else:
    nota3_com_peso = nota3 * 2
    media = (nota1 + nota2 + nota3_com_peso)/4
    print('a média do aluno é de:',media)
