numero = (input('digite um número: '))

if int(numero) < 0:
    print('erro')
 
elif int(numero) > 0: 
    # a soma recebe a função 'sum()' de soma e o 'int(digito)' vai percorrer e armazenar os numeros digitados na variavel 'numero'
     soma = sum(int(digito) for digito in numero)
     print('a soma dos numeros é de:',soma)

