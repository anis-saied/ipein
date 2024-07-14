#---------------------------------------------
# CHP 2 : Syntaxe de base de la POO 
# Ex  3 : la classe point 
#---------------------------------------------

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






