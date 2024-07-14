'''
TP3 : Les files
Groupe : Ipein/ST1/GB
Date : 04-10-2023
'''

# file.py
def creer_file():
    return []
def file_vide(f):
    return len(f)==0
def sommet(f):
    return f[0]
def taille(f):
    return len(f)
def enfiler(f,x):
    f.append(x)
    
def defiler(f):
    s = f.pop(0)
    return s

# Ex1
def afficher(f):
    t = taille(f)
    for i in range(t):
        s = defiler(f)
        print(s)
        enfiler(f,s)

def defilerJusqua(f,x):
    while taille(f)>0 and \
          sommet(f)!=x:
        defiler(f)

def appartient(f,x):
    t = taille(f)
    test = False
    for i in range(t):
        s = defiler(f)
        if s == x:
            test = True
        enfiler(f,s)
    return test

def appartient(f,x):
    from copy import copy
    f1 = copy(f)
    defilerJusqua(f1,x)
    if taille(f1)>0:
        return True
    return False

# EX 2
def nb_hamming(n):
    f2= creer_file(); enfiler(f2,1)
    f3= creer_file(); enfiler(f3,1)
    f5= creer_file(); enfiler(f5,1)
    for i in range(n):
        k = min(sommet(f2),sommet(f3),sommet(f5))
        if k==sommet(f2) : defiler(f2)
        if k==sommet(f3) : defiler(f3)
        if k==sommet(f5) : defiler(f5)
        print(k, end=", ")
        enfiler(f2,2*k)
        enfiler(f3,3*k)
        enfiler(f5,5*k)
