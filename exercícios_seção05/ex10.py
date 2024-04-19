altura = float(input('Digite sua altura: '))
sexo = (input('Digite seu sexo, sendo, masculino: "M" e feminino: "F": '))

if sexo == "F" or sexo == "f":
   res_fem = (62.1 * altura) -44,7
   print('O peso feminino ideal para sua altura é de: ',res_fem)   

elif sexo == "M" or sexo == "m":
   res_masc = (72.7 * altura) -58
   print('O peso masculino ideal para sua altura é de: ',res_masc)   

else:
   print('Digite um valor válido')