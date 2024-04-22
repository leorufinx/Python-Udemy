preco_antigo = int(input('Digite o valor do produto para sofrer alteração: '))

if preco_antigo < 50:
    preco_novo = preco_antigo + preco_antigo * 0.05

elif preco_antigo >= 50 and preco_antigo <= 100:
    preco_novo = preco_antigo + preco_antigo * 0.10

else:
    preco_novo = preco_antigo + preco_antigo * 0.15


if preco_novo < 80:
    print('Barato')

else:
    if preco_novo >= 80 and preco_novo < 120:
        print('Normal')
    
    elif preco_novo >= 120 and preco_novo < 200:
        print('Caro')
    
    else:
        print('Muito Caro')