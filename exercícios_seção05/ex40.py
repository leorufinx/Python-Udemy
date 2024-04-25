custoDeFabrica = float(input('Digite o valor de fábrica: '))

if custoDeFabrica <= 12.000:
    custoMaisDistribuidor = custoDeFabrica + custoDeFabrica * 0.05

else:
    if custoDeFabrica > 12.000 and custoDeFabrica <= 25.000:
        custoMaisDistribuidor = custoDeFabrica + custoDeFabrica * 0.10

    else:
        custoMaisDistribuidor = custoDeFabrica + custoDeFabrica * 0.15


if custoDeFabrica <= 12.000:
    print(custoMaisDistribuidor)

else:
    if custoDeFabrica > 12.000 and custoDeFabrica <= 25.000:
        custoDistribuidorImpostos = custoMaisDistribuidor + custoMaisDistribuidor * 0.15
        print(custoDistribuidorImpostos)

    else:
        custoDistribuidorImpostos = custoMaisDistribuidor + custoMaisDistribuidor * 0.20
        print(custoDistribuidorImpostos)