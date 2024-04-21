a = int(input('digite um valor: '))
b = int(input('digite um valor: '))
c = int(input('digite um valor: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('não pode ser um triângulo')

elif a == b == c:
    print('equilátero')

elif a !=b and a !=c and b !=c:
    print('escaleno')

elif a == b and b!=c or a == c and c!=b or b == c and c!=a:
    print('isóceles') 

else:
    print('erro')