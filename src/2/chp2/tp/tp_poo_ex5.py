'''
IPEIN
CHP 2 :  POO
Exercice : 5
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

    def afficher(self): # p.afficher()
        ch ="Nom : {}, prénom:{}"
        print(ch.format(self.nom, self.prenom))
        
class Travailleur(personne):
    def __init__(self, n, p, t, adr,ne,adrE,tE):
        super().__init__(n, p, t, adr)
        self.nomE = ne
        self.adrE = adrE
        self.tE = tE
    def __str__(self):
        return personne.__str__(self) + " en: {}"\
        .format(self.nomE)

class Scientifique(Travailleur):
    def __init__(self,n, p, t, adr,ne,adrE,tE,ts,ds):
        Travailleur.__init__(self, n, p, t, adr,ne,adrE,tE)
        self.ts = ts
        assert type(ds) in (tuple, list)
        self.ds = ds # list

    def __str__(self):
        ch = super().__str__()
        ch += ",ts : "+self.ts
        ch +=", ds:"+ "-".join(list(self.ds))
        return ch

  
        

t = Travailleur("n", "p","t","adr","nE","adE","tE")
print(t) # print(str(t))
s = Scientifique("n", "p","t","adr","nE","adE","tE",\
                 "exper",["info","chimie"])
print(s)