'''
IPEIN
CHP 2 :  POO
Exercice : 1
'''

class point:
    def __init__(self,x=3.0, y=4.):
        #x = float(input(
        self.x = x
        self.y = y
    def afficher(self):
        print("Point(x={},y={})".format(self.x,self.y))

class rectangle:
    def __init__(self, coinSupG, larg, long):
        assert type(CoinSupG) == point
        self.coinSupG = coinSupG
        self.larg = larg
        self.long = long
        
p1  = point()#x=3., y=4.
p1 = point(1,2)
p1 = point(1) #x=1, y=4.
p1 = point(y=1) #x=3. , y=1

boite = rectangle(point(12., 27.), 50., 35.)

def trouverCentre(rect):
    assert isinstance(rect, rectangle) #etape 1
    x = rect.coinSupG.x + rect.larg / 2 #4
    y = rect.coinSupG.y - rect.haut / 2 #4
    centre = point(x,y) #3
    return centre #2

# appel à une fonction: fonction(objet)
centre = trouverCentre(boite) 
# appel à une méthode : objet.methode()
centre.afficher()

#Q8
boite.larg *= 2
boite.haut /= 2






