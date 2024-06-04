"""
Série 1 : Rappel
Groupe : Ipein/SP3/GB
Date : 2022-11-18
Auteur : Anis SAIED
email : Anis.SAIED@pm.me
"""
import math

# Exercise 1
## Q1
def init(L):
    # vider la liste
    while len(L)>0:
        L.pop()
    #L.clear()
    # initialiser la liste par 100 valeur = 1
    for i in range(100):
        L.append(1)

# Q2
def multiple(L,i):
    ''' mettre à 0 les multiples de i (non premiers)( sauf i)'''
    for j in  range(i+1, len(L)):
        if j % i == 0 :
            L[j] = 0

# Q3
def suivant(L,i):
    ''' retourne le nombre premier qui suit i '''
    for j in range(i+1, len(L)):
        if L[j] == 1 :
            return j

# Q4
def crible(L): # signature de la fonction
    init(L)
    i = 2
    end = int(math.sqrt(len(L)))
    while i <= end:
        multiple(L,i)
        i = suivant(L,i)
    
    # extraction des nombres premiers 
    p = []
    for i in range(2,len(L)):
        if L[i] == 1:
            p+=[i]
    return p    

# Q5
def crible_rec(L,i):
    if i <= int(math.sqrt(len(L))):
        multiple(L,i)
        i = suivant(L,i)
        return crible_rec(L,i) #appel récursif
    else:
        p = []
        for i in range(2,len(L)):
            if L[i] == 1:
                p+=[i]
        return p    

## Q7 prog principal
if __name__ == "__main__":
    L = [] # L = list() # variable global
    init(L)
    p = crible_rec(L,2)#appel principal
    print(p)

    

