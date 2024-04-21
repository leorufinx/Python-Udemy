km = float(input('digite quantos quilometros foram andados: '))
litros = float(input('quantos litros foram gastos para percorrer essa distância: '))

kmPorLitro = km/litros

if kmPorLitro <= 0:
    print('digite valores válidos')

else:
    if kmPorLitro < 8:
        print('Venda o carro!')
    
    elif kmPorLitro >= 8 and kmPorLitro <= 14:
        print('ec0nômico')
    
    else:
        print('super econômico')