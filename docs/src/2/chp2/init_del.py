class Fichier:
    def __init__(self, nom):
        self.nom = nom
        print("Le fichier " + self.nom + " a été créé.")
    
    def __del__(self):
        print("Le fichier " + self.nom + " a été supprimé")

f = Fichier("mon fichier.txt")
print(f.nom)
