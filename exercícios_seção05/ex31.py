altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))

if altura < 1.20 and peso <60:
    print('A')

else:
    if altura >= 1.20 and altura <= 1.70 and peso <60:
        print('B')
    
    elif altura > 1.70 and peso <60:
        print('C')

    elif altura < 1.20 and peso >= 60 and peso <= 90:
        print('D')

    elif altura >= 1.20 and altura <= 1.70 and peso >= 60 and peso <= 90:
        print('E')

    elif altura > 1.70 and peso >= 60 and peso <= 90:
        print('F')
    
    elif altura < 1.20 and peso > 90:
        print('G')
    
    elif altura >= 1.20 and altura <= 1.70 and peso >90:
        print('H')

    elif altura > 1.70 and peso >90:
        print('I')