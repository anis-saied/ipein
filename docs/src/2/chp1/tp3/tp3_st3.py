'''
TP3 : Les files
Groupe : Ipein/ST3/GB
Date : 28-09-2023
'''
from copy import copy

# file.py
def creer_file(): return []
def file_vide(f): return len(f)==0
def sommet(f): return f[0]
def taille(f):return len(f)
def enfiler(f,x): 
    # ajouter x en fin de f
    f.append(x)
def defiler(f):
    # le sommet est à la position 0
    return f.pop(0)

# Ex1
def afficher(f):
    #afficher <=> print
    #saisir <=> input
    #renvoyer <=> return
    f1 = copy(f)
    while taille(f1)>0:
        print(sommet(f1))
        defiler(f1)

def afficher(f):
    for i in range(taille(f)):
        s = defiler(f)
        print(s)
        enfiler(f,s)
'''
def afficher(f):
    print(f)
'''
def defilerJusqua(f,x):
    while taille(f)>0 and sommet(f) != x:
        defiler(f)

def appartient(f,x):
    test = False
    for i in range(taille(f)):
        if x == sommet(f) : 
            test = True
        enfiler(f,defiler(f))
    return test

def appartient(f,x):
    f1 = copy(f)
    defilerJusqua(f1,x)
    if file_vide(f1) : return False
    return True

def appartient(f,x):
    f1 = copy(f)
    defilerJusqua(f1,x)
    return not file_vide(f1)
    #return taille(f1)

def inverser(f):
    #from pile import *
    p = creer_pile()
    # etape 1: vider f dans p
    while taille(f)>0:
        empiler(p,defiler(f))
    
    # t = taille(f)
    # for i in range(0,t):
    #     empiler(p,defiler(f))
    # etape 2 : vider p dans f
    while not pile_vide(p):
        enfiler(f,depiler(p))

def nb_hamming(n):
    f2 = creer_file(); enfiler(f2,1)
    f3 = creer_file(); enfiler(f3,1)
    f5 = creer_file(); enfiler(f5,1)
    for i in range(n):
        k = min(sommet(f2), sommet(f3), sommet(f5))
        if k == sommet(f2) : defiler(f2)
        if k == sommet(f3) : defiler(f3)
        if k == sommet(f5) : defiler(f5)
        enfiler(f2, 2*k)
        enfiler(f3, 3*k)
        enfiler(f5, 5*k)
        print(k, end=", ")