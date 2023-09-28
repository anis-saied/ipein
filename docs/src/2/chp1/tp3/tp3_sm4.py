def creer_file():
    return list()
def file_vide(f):
    return len(f)==0
def taille(f): return len(f)
def enfiler(f,x): f.append(x)
def defiler(f): 
    return f.pop(0)
def sommet(f): return f[0]

# ex1
def afficher(f):
    t = taille(f)
    for i in range(t):
        s = defiler(f)
        print(s)
        enfiler(f,s)
    