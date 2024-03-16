class point:
    def __init__(self,x,y,nom):
        self.x = x
        self.y = y
        self.nom = nom

from math import sqrt
def calculer_distance(p1,p2):
    if (type(p1)==point) and (type(p2)==point):
       return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    else:
        return None
'''  
# prog principal
n = int(input("n ="))
L = []
for i in range(n):
    L.append(point(i,i+1,"A"+str(i+1)))
print(L)

ch = "distance entre {} et {} : {}"
for i in range(len(L)-1):
    for j in range(i+1, len(L)):
        d = calculer_distance(L[i],L[j])
        print(ch.format(L[i].nom,L[j].nom,d))
    
'''
class etudiant:
    def __init__(self, math, phy, nom):
        self.nom =  nom
        self.math = math
        self.phy = phy
    def calculer_moyenne(self):
        #assert isinstance(e,etudiant)
        return (self.math + self.phy)/2
#prog ppl
n = int(input("nombre d'etudiants: "))
d = dict()
for i in range(n):
    e=etudiant(math=10+i, phy=11+i, nom="A"+str(i))
    d[e.nom] = e

somme_math = 0; somme_phy=0 
for e in d.values():
    somme_math += e.math
    somme_phy += e.phy

ch = "Moyenne math : {}, moyenne phy : {}"
ch = ch.format(somme_math/n,somme_phy/n)
print(ch)

for e in d.values():
    m = e.calculer_moyenne()
    print(e.nom," moyenne: ",m) 










