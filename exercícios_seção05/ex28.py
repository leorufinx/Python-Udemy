import math

x = int(input('digite o valor de x: '))
y = int(input('digite o valor de y: '))
z = int(input('digite o valor de z: '))

print('digite a operação desejada:')
print('(A) Geométrica')
print('(B) Ponderada')
print('(C) Harmônica')
print('(D) Aritmética')

opc = str(input('digite a operação desejada: ')).upper()

match opc:
    case "A":
        #pow eleva a raiz a 3
        #math.pow() = (base x expoente)
        #sendo a base o resultado de x * y * z
        # e o expoente será o 1/3
        geometrica = math.pow((x * y * z), 1/3)
        print(geometrica)
    
    case "B":
        ponderada = (x+(2*y)+(3*z))/6
        print(ponderada)

    case "C":
        harmonica = 1/(1/x + 1/y + 1/z)
        print(harmonica)

    case "D":
        aritmetica = (x+y+z)/3
        print(aritmetica)

    case _:
        print('digite uma operação válida')