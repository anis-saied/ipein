#IPEIN 2023/2024 - DS1 
#Exercice2.py

#Question 1 : (1.5 pts)
def somDiv(n):
    """Retourne la somme des diviseurs propres de "n"."""
    somme = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            somme += i
    return somme

#Question 2 : (1.5 pts)
def estParfait(n):
    """Teste si "n" est parfait."""
    return somDiv(n) == n

#Question 3 : (1.5 pts)
def estPremier(n):
    """Teste si "n" est premier."""
    return True if somDiv(n) == 1 else False

#Question 4 : (1.5 pts)
def estChanceux(n):
    """Teste si "n" est chanceux."""
    if n<2: return False
    for i in range(2, n-1):
        if not estPremier(n + i + i**2):
            return False
    return True

#Question 5 : (1.5 pts)
def SaisieRec(m):
    """Fonction de saisie d'un entier n"""
    try:
        n = int(input("Donner entier 0<n<="+str(m)+": "))
        if 0<n<=m: return n
        print("Erreur de saisie...")
        return SaisieRec(m)
    except:
        print("Erreur de conversion...")
        return SaisieRec(m)

#Question 6 : (2.5 pts)    
def main():
    n = SaisieRec(1000)
    try: f = open("Resultat.txt","w")
    except:
        print("Erreur fichier...")
        return
    LPremier = list()
    LParfait = list()
    LChanceux = []
    for i in range(1,n+1):
        if estPremier(i): LPremier.append(i)
        if estParfait(i): LParfait.append(i)
        if estChanceux(i): LChanceux.append(i)
    f.write("LPremier = " + str(LPremier) + "\n")
    f.write("LParfait = " + str(LParfait) + "\n")
    f.write("LChanceux = "+ str(LChanceux) + "\n")
    f.close()
  
