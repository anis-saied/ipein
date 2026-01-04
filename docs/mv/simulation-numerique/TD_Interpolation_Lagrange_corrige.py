#Simulation numérique : Python
#Interpolation polynomiale de Lagrange

#Correction de la série
#Institut : IPEIN
#email    : anis_saied@hotmail.com

import numpy as np

#Q1
def produit(s):
	"""
	retourne le produit des éléments d’une séquence s
	"""
	p = 1
	for i in s: 
		p *= i
	return p
	
#Q2
def interpolation_lagrange(X, Y, x):
	"""
	implémentation de la méthode de Lagrange 
	X : séquence (X_i) de taille n+1 elements(nombre de points)
	Y : séquence, Y(X_i) de taille n+1 elements(nombre de points)
	x : point
	retourne une estimation du polynôme de lagrange au point x : P(x)
	"""
	n = len(Y)
	lf = 0
	for i in range (n):
		l=[]
		for j in range(n):
			if j != i :
				l.append((x-X[j])/(X[i]-X[j]))
		lp = produit(l)
		lf+=lp*Y[i]
	return lf
	

	
#Q3
#tableaux des mesures
Temperature = np.array([0.0, 5.0, 10.0, 15.0, 20.0])
MasseVol = np.array([999.87, 999.99, 999.73, 999.13, 998.23])

#Q4
#tableau de l’intervalle des abscisses des estimations
x=np.arange(0,20.1,0.1)

#Q4.1
#calcul des estimations avec la fonction implémentée dans une liste C0
C0=[]
for i in x:
	estim=interpolation_lagrange(Temperature,MasseVol,i)
	C0.append(estim)
	
#Q4.2
#chargement de la fonction lagrange
from scipy.interpolate import lagrange

#calcul des estimations de l’importée dans un vecteur C
P=lagrange(Temperature,MasseVol)
C=P(x)


#Q5
#chargement de pyplot
import matplotlib.pyplot as plt

#traçage graphique des trois courbes
plt.grid() #avec grille
plt.plot(Temperature,MasseVol,'r',label="mesures")#traçage de la 1 ère courbe
plt.plot(x,C0,'b',label="lagrange_impl")#traçage de la 2 ème courbe
plt.plot(x,C,'g',label="lagrange_import")#traçage de la 3 ème courbe
plt.legend() #pour afficher les labels
plt.show()#affichage à l’écran


