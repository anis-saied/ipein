"""
Série 1 : Rappel
Date : 06-09-2023
Groupe : Ipein/ST1/GB
"""
import math

# Exercice 1
## Q1
def init(L):
    #print("id(L) local avant création=",id(L))
    #L=[]
    #print("id(L) local après création =",id(L))
    #L= [1 for i in range(100)]
    
    #vider la liste
    while len(L)>0:
        L.pop()
    #initialiser la liste
    for i in range(100):
        L.append(1)
    #return L

def init1():
    return [1]*100
## Q2  
def multiple(L,i):#signature : multiple(L,i)
    for j in range(i+1,len(L)):
        if j % i == 0:
            L[j] = 0
    
## Q3 
def suivant(L,i):
    '''
    le nombre premier qui suit l'indice i
    '''
    for j in range(i+1,len(L)):
        if L[j] == 1:
            return j
## Q4
def crible(L):
    init(L)
    
    i = 2
    while i <= int(math.sqrt(len(L))):
        multiple(L,i)
        i = suivant(L,i)
    #extraction des nombres premiers
    p = []
    for i in range(2,len(L)):
        if L[i]==1:
            p.extend([i]) # p += [i]
    return p #p[2:]

## Q5
def crible_rec(L,i):
    if i <= int(math.sqrt(len(L))):
        multiple(L,i)
        i = suivant(L,i)
        return crible_rec(L,i)
    else:
        print(L)
        p = [i for i in range(2,len(L)) if L[i]==1]
        print(p)
        return p

## prog principal
L = [] #list()
init(L)
p = crible_rec(L,2)
print(p)

"""
init(L)
multiple(L,2)
print(L)
p = crible(L)
print(p)
print("avant L=",L)
print("id(L) global =",id(L))
r = init(L)
print("id(L) global=",id(L))
print("après L=",L)
print("id(r) global=",id(r))
print("r=",r)
"""

