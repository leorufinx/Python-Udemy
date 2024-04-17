
#leia o salario de um trabalhador e o valor da prestação de um empréstimo que se for maior que 20%
#do salário imprima: 'emprestimo nao concedido', caso contrário imprima: 'emprestimo condedido'
# *0.20

salario = float(input('digite seu salário: '))
emprestimo = float(input('digite o valor do emprestimo desejado: '))

salarionovo = 0.2 * salario + salario

if salarionovo < emprestimo:
    print('empréstimo não concedido')
else: 
    print('empréstimo concedido!')