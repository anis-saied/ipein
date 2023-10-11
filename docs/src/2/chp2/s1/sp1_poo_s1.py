#-----------------------------------------------------
# Groupe : SP1 
# Chp 2 : POO Partie 1
# Date : 09-10-2023
# Email : anis_saied@hotmail.com
# website : https://anis-saied.github.com/ipein
#-----------------------------------------------------
class Rectangle:
    def __init__(self,long,larg,nom):
        self.largeur = larg
        self.longueur = long
        self.nom = nom

    def calculer_surface(self):
        s = self.largeur * self.longueur
        return s
    def __del__(self):
        print("destruction de :"+self.nom)
        
rectangle1 = Rectangle(5,3,"r1")
print(rectangle1.calculer_surface())
rectangle2 = Rectangle(4,6,"r2")
print(rectangle2.calculer_surface())
del rectangle2
rectangle1 = 5
Rectangle(4,6,"r3")
#-----------------------------------------------------
class voiture:
    def __init__(self,marque=''):
        if marque == '':
            marque = input("marque ?: ")
        self.marque = marque
    def demarrer(self):
        print("La voiture démarre!")
    def arreter(self):
        print("La voiture s'arrête!")
v1 = voiture('kia')
v1.demarrer()
v1.arreter()
#-----------------------------------------------------
class point:
    def __init__(self,x,y,nom):
        self.x = x
        self.y = y
        self.nom = nom
        
n = 10
L = []

for i in range(n):
    L.append(point(i,i+1,str(i)))
    
from math import sqrt
def distance(p1,p2):
    assert type(p1) == point
    assert type(p2) == point
    return sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    
for i in range(n-1):
    for j in range(i+1,n):
        d= distance(L[i],L[j])
        print("{} - {}={}"\
              .format(L[i].nom,L[j].nom,d))
#-----------------------------------------------------





