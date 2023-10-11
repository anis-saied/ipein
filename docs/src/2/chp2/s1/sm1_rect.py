class Rectangle :
    # self:instance de classe Rectangle à initialiser
    def __init__(self, long , larg,nom):
        self.longueur = long
        self.largeur = larg
        self.nom = nom
        print("appel au constructeur")

    def calculer_surface(self):
        s = self.largeur * self.longueur
        return s
    def __del__(self):
        print("rectangle est détruit")

R1 = Rectangle(5,3,"r1")
R2 = Rectangle(4,6,"r2")

print(R1.calculer_surface())
print(R2.calculer_surface())

# Ex2 : Voiture -----------------------
class Voiture:
    def __init__(self,marque=''):
        if marque == '':
            marque = input("marque ? : ")
        self.marque = marque
    def demarrer(self):
        print("Voiture démarre.")
    def arreter(self):
        print("Voiture s'arrête.")

v1 = Voiture("kia")
v1.demarrer()
v1.arreter()
v2 = Voiture()

# Ex3 : Point -----------------------












