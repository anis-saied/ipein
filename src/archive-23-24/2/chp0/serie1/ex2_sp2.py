'''
Série 1 : rappel
Groupe : SP2/GB
'''
# Exercice 2
def saisie_deg(): 
    while 1:
        try :
            n = int(input("n="))
            if n>0:
                return n
        except :
            continue
    
def saisie_poly(n):
    p = [None]* (n+1)
    for i in range(n+1):
        while 1:
            try:
                c = float(input("P[{}]= ".format(i)))
                if (i<n) or (i==n and c!=0):
                    p[i] = c
                    break # stop while
            except:
                print("Erreur")
    return p

def derive(p): return [p[i]*i for i in range(1,len(p))]

def opp_poly(p): return [-c for c in p]

def add_poly(p1,p2):
    n1,n2 = len(p1),len(p2)
    p = [p1[i]+p2[i] for i in range(min(n1,n2))]
    p += p2[n1:] if n2 > n1 else p1[n2:]
    #opérateur ternaire : T1 if cond else T2
    return p

   
def mul_poly(p1,p2):
    n1 = len(p1)-1
    n2 = len(p2)-1
    p = [0] * (n1+n2+1)
    for i in  range(n1+1):
        for j in range(n2+1):
            p[i+j] += p1[i] * p2[j]
    return p

# a terminer
def suite_poly(p,k):
    assert type(k)==int and k>=0
    assert type(p)==list

    if k==0: sp_k = p
    elif k==1: sp_k = opp_poly(derive(p))
    else:
        sp_k = p
        sp_k1 = opp_poly(derive(p))
        for i in range(2,k+1):
            q = mul_poly (sp_k1 , sp_k)
            sp_k2 = add_poly(mul_poly(q , sp_k1),sp_k)

    return sp_k
