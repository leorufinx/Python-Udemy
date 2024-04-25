valor_venda = float(input('digite o valor da venda: '))


if valor_venda >= 100.000:
   vendaComComissao = 700 + valor_venda * 0.16
   valor_formatado = "${:,.2f}".format(vendaComComissao)
   print(valor_formatado)

elif valor_venda < 100.000 and valor_venda >= 80.000:
   vendaComComissao = 650 + valor_venda * 0.14
   valor_formatado = "${:,.2f}".format(vendaComComissao)
   print(valor_formatado)

elif valor_venda < 80.000 and valor_venda >= 60.000:
   vendaComComissao = 600 + valor_venda * 0.14
   valor_formatado = "${:,.2f}".format(vendaComComissao)
   print(valor_formatado)

elif valor_venda < 60.000 and valor_venda >= 40.000:
   vendaComComissao = 550 + valor_venda * 0.14
   valor_formatado = "${:,.2f}".format(vendaComComissao)
   print(valor_formatado)

elif valor_venda < 40.000 and valor_venda >= 20.000:
   vendaComComissao = 500 + valor_venda * 0.14
   valor_formatado = "${:,.2f}".format(vendaComComissao)
   print(valor_formatado)

else:
   vendaComComissao = 400 + valor_venda * 0.14
   valor_formatado = "${:,.2f}".format(vendaComComissao)
   print(valor_formatado)
