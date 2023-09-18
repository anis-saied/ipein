"""
Série 1 : Rappel
Date : 14-09-2023
Groupe : Ipein/SM4/GB
"""
# Exercice 2
def saisie_deg():
    while 1:
        try:
            n = int(input("entier n >0, n="))
            if n>0:
                return n
        except : 
            print("Erreur...")

def saisie_poly(n):
    p = [] #liste represente un polynome
    for i in range (n+1):
        while 2:
            try:#essayer
                coef = float(input("coef="))
                if (i<n) or (i==n and coef != 0):
                    p.append(coef)
                    break # arrêter while
            except : #s'il y a une exception
                continue
    return p

def derive(p):
    d = []
    for i in range(1,len(p)):
        d.append(p[i]*i)
    return d

def opp_poly(p):
    return [-c for c in p]

def add_poly(p1,p2):
    n1, n2 = len(p1), len(p2)
    p = [p1[i] + p2[i] for i in range(min(n1,n2))]
    p += p1[n2:] if n1>n2 else p2[n1:]
    
    while len(p)>0  and p[-1]== 0: 
        p.pop(-1)

    return [0] if p==[] else p

def mul_poly(p1,p2):
    n1, n2 = len(p1), len(p2)
    p  = [0]*(n1 + n2 - 1)
    for i in range(n1):
        for j in range(n2):
            p[i+j] += p1[i] * p2[j]
    return p

def sp(p,k):
    assert type(k)==int and k>=0
    assert type(p)==list 
    if k==0 : return p
    elif k==1 : return opp_poly(derive(p))
    else:
        sp0 = p
        for i in range(2,k+1):
            sp1 = opp_poly(derive(sp0))
            q = mul_poly(sp1,sp0)
            sp2 = add_poly(mul_poly(q , sp1), sp0)
            sp0 = sp1
            sp1 = sp2

    return sp2

