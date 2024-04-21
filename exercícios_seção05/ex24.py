valor_produto = float(input('Digite o valor para calcular o imposto: '))
estado = str(input('Escolha o estado: "SP" "MG" "RJ" MS": ')).upper()
print(estado)

if estado != "SP" and estado != "MG" and estado != "RJ" and estado != "MS":
    print('Digite um estado válido')
else:
    if estado == "SP":
        imposto = valor_produto + valor_produto * 0.12
        print("o valor do produto com o imposto aplicado em São Paulo é de:",imposto)

    elif estado == "MG":
        imposto = valor_produto + valor_produto * 0.07
        print('o valor do produto com imposto aplicado em Minas Gerais é de:',imposto)
    
    elif estado == "RJ":
        imposto = valor_produto + valor_produto * 0.15
        print('o valor do produto com imposto aplicado no Rio de Janeiro é de:',imposto)
    
    elif estado == "MS":
        imposto = valor_produto + valor_produto * 0.08
        print('o valor do produto com imposto aplicado no Mato Grosso é de:',imposto)