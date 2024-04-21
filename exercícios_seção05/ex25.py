import math

a = float(input('digite o coeficiente a:'))
b = float(input('digite o coeficiente b:'))
c = float(input('digite o coeficiente c:'))

delta = ((b*b) - 4) *a*c

if delta <0:
    print('Não existe raiz')

else:
    if delta == 0:
        x = (-b + math.sqrt(delta))/(2 *a)
        print(x, 'Raiz única')
    
    elif delta >= 0:
        x1 = (-b + math.sqrt(delta))/(2 *a)
        x2 = (-b - math.sqrt(delta))/(2 *a)
        print('x1:',x1)
        print('x2:',x2)