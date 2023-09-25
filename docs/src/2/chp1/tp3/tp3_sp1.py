'''
TP3 : Les files
Groupe : Ipein/SP1/GB
Date : 24-09-2023
'''
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
    for i in range(taille(f)):
        x = defiler(f)
        print(x)
        enfiler(f,x)

def defiler_jusqua(f,x):
    while taille(f)>0 and sommet(f)!=x:
        defiler(f)
    # sortie de while : 
    # if file vide or sommet(f)==x

def appartient(f,x):
    from copy import copy
    f1 = copy(f)
    defiler_jusqua(f1,x)
    if file_vide(f1): return False
    return True


