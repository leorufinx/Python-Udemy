""" 
'and' =  && (java)
'or' = || (Java)
'not' = ! (Java)
'is' = == (Java)
"""

ativo = True
logado = False


if ativo and logado:
    print('Bem-vindo Usuário!')
else:
    print('Ative sua conta, por favor cheque seu e-mail')


if ativo or False:
    print('Bem-vindo Usuário!')
else:
    print('Ative sua conta, por favor cheque seu e-mail')


if not ativo:
    print('Ative sua conta, por favor cheque seu e-mail')
else:
    print('Bem-vindo, Usuário!')


if ativo is True:
    print('Bem-vindo Usuário!')
else:
    print('Ative sua conta, por favor cheque seu e-mail')



