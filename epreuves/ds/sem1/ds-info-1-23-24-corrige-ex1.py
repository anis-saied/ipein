#IPEIN 2023/2024 - DS1 
#Exercice1.py

#Question 1 : (2.0 pts)
def SIC_it(n):
    s = 0
    for i in range(1,n+1):
        s += 1/i**2
    return s

#Question 2 : (2.0 pts)
def SIC_rec(n):
    if n == 1: return 1
    else: return 1/n**2 + SIC_rec(n-1)

#Question 3 : (2.0 pts)
#
#   1/16+1/9+1/4+1 = 1.42
#     <-------
#             |     
#             |     1/9+1/4+1 = 1.36
#      SIC_rec(4) <-------
#           |             |      
#           |             |     1/4+1=1.25
#            -----> SIC_rec(3) <-------     
#                        |             |          
#                        |             |         1
#                         ------> SIC_rec(2) <-------  
#                                      |             |
#                                      |             |
#                                       -----> SIC_rec(1)                                            
#                                                 
# Dans ce cas la pile d'appels récursifs doit être de taille 3 cases mémoires.

#Question 4 : (2.0 pts soit 0.5 par question)
#a- Calcul du coût et complexité temporelle pour SIC_it(n):
# Coût = 4n+2 soit une complexité temporelle linéaire O(n)

#b- Calcul du coût et complexité spatiale pour SIC_it(n):
# cette fonction utilise 3 variables n, i et s
# d'où Coût = 3 unités de mémoire
# soit une complexité spatiale constante O(1)

#c- Calcul du coût et complexité temporelle pour SIC_rec(n):
# SIC_rec(n) implique (n-1) appels récursifs et dans chaque appel il y a
# 1 division + 1 puissance + 1 addition = 3 opérations (si on néglige
# la comparaison et return de chaque appel)
# d'où Coût = 3n soit une complexité temporelle linéaire O(n)

#d- Calcul du coût et complexité spatiale pour SIC_rec(n):
# SIC_rec(n) implique (n-1) appels récursifs et pour chaque appel on
# sauvegarde l'argument "n" dans la pile des appels (ici on néglige
# l'adresse de retour)...
# d'où Coût = n-1 cases mémoires dans la pile d'appels
# soit une complexité spatiale linéaire O(n)

#Question 5 : (2.0 pts)
from math import pi
def main():
    while 1:
        try:
            n = int(input("Donner n>0:"))
            if n>0: break
        except: continue
    r = SIC_rec(n)
    pi_cal = (r*6)**0.5
    erreur = 100*(pi-pi_cal)/pi
    print("pi={:5.3f} avec un taux d'erreur = {:5.2f}%".format(pi_cal,erreur))
    
