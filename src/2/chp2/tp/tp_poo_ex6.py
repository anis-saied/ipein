'''
IPEIN
CHP 2 :  POO
Exercice : 6
'''

class personne:
    def __init__(self, nom, prenom, tel, adresse):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.adresse = adresse

    def __str__(self): 
        # str(p); print(p) => print(str(p))  
        # p.__str__()  
        # Presonne.__str__(p)
        ch ="Nom : {}, prénom:{}"
        return ch.format(self.nom, self.prenom)


class carnetAdresse:
    def __init__(self):
        self.contacts = []
    def ajouter_contact(self,contact):
        assert type(contact) == personne
        self.contacts.append(contact)  
    def __str__(self):        
        L = [str(p) for p in self.contacts]       
        return "\n".join(L)
    
    def chercher_contact(self, nom, prenom=None):
        for p in self.contacts:
            if p.nom == nom and \
               (prenom==None or p.prenom == prenom):
                print(p)


class Pile:
    def __init__(self):
        self.data = []

    def empiler(self, element):
        self.data.append(element)