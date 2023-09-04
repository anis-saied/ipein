P1 = [-1, 2, 0, 3]  #degre 3
P2 = [2, 1, -2, 0, 3]   #degre 4
#Q1
def Saisie_deg():
    while True:
        try:
            n = int(input("donner le degre du polynome:"))
            if type(n) == int and n>0:
                break
        except ValueError:
            continue
    return(n)
#Q2
def Saisie_poly(deg):
    P = []
    for i in range(deg+1):
        while True:
            try:
                coef=float(input("Donner le coefficient P["+str(i)+"]="))
            except ValueError:
                print ("coefficient invalide")
            else:
                #il faut éviter d'avoir un coef nul en fin du poly
                if i<deg or (i==deg and coef !=0):
                    P.append(coef)
                    break #arrêt de la boucle while
    return(P)



#Q3
def derive(p):
    return [i * p[i] for i in range(1,len(p))]

#Q4
def opp_poly(P):
    return [-i for i in P]

#Q5
def add_poly(p1,p2):
    return [
    p1[i]+p2[i] if i<len(p1) and i<len(p2) else 
    p1[i] if i<len(p1) and i>=len(p2) else p2[i] 
    for i in range(max(len(p1),len(p2)))
    ]

#Q6
def mul_poly (P1, P2, deg1, deg2):
    P = [0] * (deg1+ deg2 + 1)
    for i in range(deg1+1):
        for j in range(deg2+1):
            P[i+j] += P1[i]*P2[j]
    return(P)

#Q7
deg = Saisie_deg()
P = Saisie_poly(deg)
print("P = ", P)
D = derive(P)
print("D = ", D)
O = opp_poly(P)
print("O = ", O)
A = add_poly(P,D)
print("A = ", A)
M = mul_poly(P,D,len(P)-1,len(D)-1)
print("M = ", M)



