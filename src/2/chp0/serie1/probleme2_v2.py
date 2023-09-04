# Solution 1

def add_poly (P1, P2, deg1, deg2):
    S = []
    m = min(deg1,deg2)

    for i in range(m+1):
        S.append(P1[i]+P2[i])
    if m == deg1: S = S+P2[m+1:]
    if m == deg2: S = S+P1[m+1:]

    return(S)


# Solution 2

def add_poly (P1, P2, deg1, deg2):

    while len(P1) != len(P2):
        if len(P1) < len(P2):
            P1.append(0)
        elif len(P2) < len(P1):
            P2.append(0)

    return [P1[i] + P2[i] for i in range(len(P1))]

# Solution 3

# Opérateur ternaire
# Résultat_if_cond_True if condition else Résultat_if_cond_False

def add_poly (p1, p2, n1, n2):

    p11 = p1 + [0] * (n2-n1) if n2>n1 else p1
    p21 = p2 + [0] * (n1-n2) if n1>n2 else p2
    
    p3 = [0] * len(p11)

    for i in range(len(p3)):
        p3[i] = p11[i] + p21[i]

    return p3

# Solution 4

def add_pol(p1,p2):
	return [
                p1[i]+p2[i] if i<len(p1) and i<len(p2) else 
                p1[i] if i<len(p1) and i>=len(p2) else p2[i] 
                for i in range(max(len(p1),len(p2)))
                ]
