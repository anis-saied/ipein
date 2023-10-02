'''
TP3 : Les files
Groupe : Ipein/SM1/GB
Date : 25-09-2023
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
    # ajouter x en fin de f
    f.append(x)
def defiler(f):
    # le sommet est à la position 0
    return f.pop(0)


# Ex1
def afficher(f): 
    for i in range(taille(f)):
        x = defiler(f)
        print(x)
        enfiler(f,x)

def defilerJusqu(f,x):
    while taille(f)>0 and x!=sommet(f):
        defiler(f)

def appartient(f,x):
    from copy import copy
    f1 = copy(f)
    defilerJusqu(f1,x)
    return taille(f1)

# Pile
def creer_pile():
    return list()#[]
    
def pile_vide(p): return len(p)==0 #p==[]

def sommet(p):
    if not pile_vide(p):
        return p[-1]
    else:
        raise Exception("Pile vide")
# prog ppl
p = creer_pile()
try:
    s = sommet(p)
except:
    print("Pas sommet: pile vide")
else:
    print("sommet:",s)

def taille(p): return len(p)
def empiler(p,x): p.append(x)
def depiler(p):
    if not pile_vide(p):
        return p.pop()
    else:
        raise Exception("Pile vide")
    
def inverser_file(f):
    #from pile import *
    p = creer_pile()
    while not file_vide(f):
        empiler(p,defiler(f))

    while not pile_vide(p):
        enfiler(f,depiler(p))


def afficher(n):
    f2 = creer_file()
    f3 = creer_file()
    f5 = creer_file()
    enfiler(f2,1)
    enfiler(f3,1)
    enfiler(f5,1)
    for i in range(n):
        k = min(sommet(f2),sommet(f3),
                sommet(f5))
        print(k)
        if sommet(f2)==k: defiler(f2)
        if sommet(f3)==k: defiler(f3)
        if sommet(f5)==k: defiler(f5)
        enfiler(f2,2*k)
        enfiler(f3,3*k)
        enfiler(f5,5*k)
# Ex 4
def creer_file(n): return [0,0,[0]*n]
def taille(f): return f[0]-f[1]
def file_vide(f): return taille(f)==0
def sommet(f): return f[2][f[1]]
def enfiler(f,x):
    n = len(f[2])
    if taille(f)< n:
        Q = f[0]% n
        f[2][Q] = x
        f[0]+=1
def defiler(f):
    if taille(f)>0:
        t = f[1]% len(f[2])
        s = f[2][t]
        f[1]+=1
        return s

        
    






