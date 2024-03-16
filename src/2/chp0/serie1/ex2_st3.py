'''
Série 1 : Rappel
Date : 14-09-2023
Groupe : ipein/st3/GB
'''
# Exercice 2
## Q1
def saisie_deg(): 
    while 11:
        try:
            n = int(input("n="))
            if n>0: break #return n
        except :
            print("Erreur : n invalide.")
    return n

def saisie_poly(n): 
    p = [None] * (n+1)
    for i in range(n+1):
        while 1:
            try:
                coef = float(input("coef="))
                if (i <n) or (i==n and coef != 0) :
                    p[i] = coef
                    break
            except ValueError: 
                continue # repeter =>while
    return p

def derive(p): return [p[i]* i for i in range(1, len(p))]
def opp_poly(p): return [-coef for coef in p]
def add_poly(p1,p2): 
    n1,n2 = len(p1), len(p2)
    p = [p1[i]+p2[i] for i in range(min(n1,n2))]
    p += p1[n2:] if n1>n2 else p2[n1:]
    return p
def mul_poly(p1,p2):pass
def main(): 
    n = saisie_deg()
main()
