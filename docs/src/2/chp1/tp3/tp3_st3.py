'''
TP3 : Les files
Groupe : Ipein/ST3/GB
Date : 28-09-2023
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