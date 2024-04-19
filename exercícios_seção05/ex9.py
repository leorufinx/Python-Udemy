salario = float(input('digite seu salário: '))
emprestimo = float(input('digite o valor do emprestimo desejado: '))

salarionovo = 0.2 * salario + salario

if salarionovo < emprestimo:
    print('empréstimo não concedido')
else: 
    print('empréstimo concedido!')