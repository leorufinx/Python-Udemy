import random

numQuestao = 5
numAcertos = 0

for _ in range(numQuestao):
    a = random.randint(1,100)
    b = random.randint(1,100)
    res_user = int(input(str(a)+'+'+str(b)+' :'))
    
    if res_user == a + b:
        numAcertos +=1

print('O numero de acertos foi:',numAcertos,'/',numQuestao)
         
