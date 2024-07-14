'''
Série 1 : Rappel
Date : 09-09-2023
Groupe : ipein/sp2/GB
'''
from math import sqrt

# Exercice 1
# Q1
def init(L):# val local
   #print('var local avant création: id(L)=',id(L))
   L = [1] * 100
   #print('var local après création: id(L)=',id(L))
   return L

# Q2
def multiple(L,i): 
    for j in range(i*2, len(L)):
       if j % i == 0:
          L[j]=0

# Q3
def suivant(L,i):
    '''retourne l'entier premier svt après i '''
    '''
    for j in range(i+1,len(L)):
        if L[j]: # != 0: 
            return j
    '''
    j = i+1
    while j<len(L):
        if L[j]: return j
        else: j+=1
# Q4
def crible(L):
    L = init(L)
    i = 2
    
    while i <= int(sqrt(len(L))):
        multiple(L,i)
        i = suivant(L,i)
    # extraction des nombres premiers  
    return [i for i in range(2,len(L)) if L[i]]

# Q6
def crible_rec(L,i): # signature = entête de la fct
    if i <= int(sqrt(len(L))):    
        multiple(L,i)
        i = suivant(L,i) # i = nb premier svt
        return crible_rec(L,i) # appel récursif
    else:
        p= [i for i in range(2,len(L)) if L[i]]
        return(p)

# prog principal
L=[] # var global
L = init(L)
x=crible_rec(L,2) # appel principal
print("x=",x)


"""
#print('var global avant init: id(L)=',id(L))
L=init(L)
multiple(L,2)
j = suivant(L,2)
#print('var global après init: id(L)=',id(L))
print(j)
"""