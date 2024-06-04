'''
IPEIN
CHP 2 :  POO
Exercice : 10
'''
class PolyCreux():
    def __init__(self):
        self.data ={}
    def ajout_monome(self, monome={}):
        if len(monome)==0:
            #siaie dég
            while 1:
                try:
                    deg= int(input("deg="))
                    if deg>=0:
                        break
                except:
                    continue
            #siaie coef
            while 1:
                try:
                    coef= float(input("coef="))
                    if coef!=0:
                        break
                except:
                    continue            
        #ajouter monome à data
        else: #if len(monome)!=0
            coef = list(monome.values())[0]
            deg = list(monome.keys())[0]
        self.data[deg]=coef
    def degree(self):
        return max(self.data.keys())
    def __call__(self,x0):
        s=0
        for deg,coef in self.data.items():
           s+= coef * x0 **deg
        return s
    def __add__(self,other):
        assert type(other)==PolyCreux
        p =PolyCreux()
        p.data = self.data
        for deg,coef in other.data.items():
            if deg not in p.data:
                p.ajout_monome({deg:coef})
            else:
                s = coef + p.data[deg]
                if s != 0:
                    p.ajout_monome({deg:s})
                else:
                    del p.data[deg]
                    
        return p
    
#tester le code    
p = PolyCreux()
p.data={1:2,3:4}
q = PolyCreux()
q.data={1:2,3:-4,5:4}
#appel à __call__ : objet(x0)
print(p(0))
pq = p+q
print(pq.data)

