"""
Série 1
Groupe : SM1
date : 04-09-2023
"""
# Ex 1
## Q1
def init(L):
    L = []
    for i in range(100):
        L.append(1)
    return L
## Q2
def multiple(L,i):
    for j in range(i+1, len(L)):
        if j % i == 0:
            L[j] = 0
## Q3
def suivant(L,i):
    j = i + 1
    while L[j]== 0:
        j += 1
    return j
    # return L.index(1,i+1)
    
## Q4
def crible(L):
    L= init(L)
    i= 2
    from math import sqrt
    while i <= int(sqrt(len(L))):
        multiple(L,i)
        i = suivant(L,i)
    
    p = [i for i in range(2,len(L)) if L[i]==1]
    return p
## Q5
from math import sqrt
def crible_rec(L,i):

    if i <= int(sqrt(len(L))):
        multiple(L,i)
        i = suivant(L,i)
        return crible_rec(L,i)
    else:
        p = [i for i in range(2,len(L)) if L[i]==1]
        return p

## prog principal
L = []
L= init(L)
p=crible_rec(L,2)
print(p)




