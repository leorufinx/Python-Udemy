n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))
n3 = int(input('digite um número: '))

if n1 <= n2 <= n3:
    print('os numeros digitados em ordem crescente são: ',n1,n2,n3)

elif n1 <= n3 <=n2:
    print('os numeros digitados em ordem crescente são: ',n1,n3,n2)

elif n2 <= n1 <= n3:
    print('os numeros digitados em ordem crescente são: ',n2,n1,n3)

elif n2 <= n3 <= n1:
    print('os numeros digitados em ordem crescente são: ',n2,n3,n1)

elif n3 <= n1 <= n2:
    print('os numeros digitados em ordem crescente são: ',n1,n2,n3)

else:
    print('os numeros digitados em ordem crescente são: ',n3,n2,n1)


""" 
             forma mais simples de fazer: 

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    sorted_nums = sorted([num1, num2, num3])
    print("Números em ordem crescente:", sorted_nums) 
    
"""