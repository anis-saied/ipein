'''
TP3 : Les files
Groupe : Ipein/SP2/GB
Date : 30-09-2023
'''

#https://anis-saied.github.io/ipein
#file.py
def creer_file(): return []
def taille(f): return len(f)
def sommet(f): f[0]
def file_vide(f): return len(f)==0
def enfiler(f,x): f.append(x)
def defiler(f): return f.pop(0)

# Ex 1
from copy import copy
def afficher(f):
    f1 = copy(f)
    #tant qu'il reste des elements dans f
    while not file_vide(f1):
        #retirer le sommet de f
        s = defiler(f1)
        #afficher le sommet retiré
        print(s)

def affiher(f):
    for i in range(taille(f)):
        s = defiler(f)
        print(s)
        enfiler(f,s)

def defilerJusqua(f,x):
    # à la fin :
    # f = [] , if x n'existe pas
    # f = [x,*,*,*] if x existe
    
    while not file_vide(f) and sommet(f)!=x:
        defiler(f)

def appartient(f,x):
    f1 = copy(f)
    defilerJusqua(f1,x)
    if file_vide(f1): return False
    return True

from pile import *
def inverser(f):
    #inverser les elements de f avec une pile
    p = creer_pile()
    # vider f dans p
    while not file_vide(f):
        empiler(p,defiler(f))
    # vider p dans f
    while not pile_vide(p):
        enfiler(f,depiler(p))

# Ex 2
def nb_hamming(n):
    f2 = creer_file();enfiler(f2, 1)
    f3 = creer_file();enfiler(f3, 1)
    f5 = creer_file();enfiler(f5, 1)
    for i in range(n):
        k = min(sommet(f2),sommet(f3),sommet(f5))
        print(k,end=", ")
        for f in (f2,f3,f5):
            if k == sommet(f):
                defiler(f)
        enfiler(f2, 2*k)
        enfiler(f3, 3*k)
        enfiler(f5, 5*k)
# ex 3
def creer_file(n):pass
def sommet(f):pass
def taille(f):pass
def file_vide(f):pass
def enfiler(f,x):pass
def defiler(f): pass