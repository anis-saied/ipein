"""
Série 1: Rappel
Classe : SP1_GB
Date : 04-09-2023
"""
from math import sqrt

#Exercice 1
# Q1
def init(L):
    #L = []
    while len(L)!=0:
        L.pop()
    for i in range(100):
        L.append(1)
    print("id(L)local:",id(L))
    return None # None est retournée implicitement

#Q2
def multiple(L,i):
    for j in range(i+1,len(L)):
        if j % i == 0 :
            L[j] = 0
# Q3
def suivant(l,i):
    for j in range(i+1,len(L)):
        if L[j] == 1:
            return j
def crible(L):
    i = 2
    
    while i < int(sqrt(len(L))):
        multiple(L,i)
        i=suivant(L,i)
    #mth 1
    """
    p = []
    for i in range(2,len(L)):
        if L[i]==1 : p.append(i)  
    return p
    """
    # mth 2
    return [i for i in range(2,len(L)) if L[i]==1]

def crible_rec(L,i):
    if i <= int(sqrt(len(L))):
        multiple(L,i)
        i=suivant(L,i)
        return crible_rec(L,i)
    else:
        return [i for i in range(2,len(L)) if L[i]==1]
    
#anis-saied.github.io/ipein

#prog principal
L = []
init(L)
i=2
p = crible_rec(L,i)
print(p)

"""
print("id(L)global:",id(L))
print("avant : ",L)
L1 = init(L)
print("id(L)global:",id(L))
print("après : ",L)
print("L1=",L1)
"""
