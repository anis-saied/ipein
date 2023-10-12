class Voiture:
    compteur = 0
    
    def __init__(self, marque):
        self.marque = marque
        Voiture.compteur += 1
    
    @classmethod
    def nombre_total(cls):
        return cls.compteur

# Utilisation des méthodes de classe
voiture1 = Voiture("Toyota")
voiture2 = Voiture("Honda")
print(Voiture.nombre_total())  # Appel de la méthode de classe sur la classe
