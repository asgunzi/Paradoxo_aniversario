

import random 

trials = 1000 
N = 23

#Vamos analisar um caso
#Sorteia o dia
lst_dias = [random.randint(1, 365) for _ in range(N)]
lst_dias.sort(reverse = False)
print(lst_dias)


#--------------------------
#Verifica quantas repetições há em 1000 sorteios
def has_repetition(lst):
    seen = set()
    for dia in lst:
        if dia in seen:
            return True
        seen.add(dia)
    return False

count_repetitions = 0
for _ in range(trials):
    lst_dias = [random.randint(1, 365) for _ in range(N)]
    if has_repetition(lst_dias):
        count_repetitions += 1


print(f'Em {trials} sorteios de {N} dias, houve repetições em {count_repetitions} casos.')
print(f'Probabilidade de haver repetições (simulação): {100*count_repetitions/trials:.2f}%') 



#=============================

prod = 1
for p in range(2, N+1):
    prod = prod*(365 - p+1)/(365)

print('=============')
print(f'Probabilidade de não haver repetições: {100*prod:.2f}%')
print(f'Probabilidade de haver repetições: {100*(1 - prod):.2f}%')