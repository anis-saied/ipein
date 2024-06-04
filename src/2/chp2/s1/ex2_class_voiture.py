#---------------------------------------------
# CHP 2 : Syntaxe de base de la POO 
# Ex  2 : la classe Voiture 
#---------------------------------------------

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














