---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
date: 01-10-2023
slug: /informatique/poo/seance-2/surcharge_methodes
sidebar_position: 5
last_update:
  date: 2026-01-04
  author: Anis
---

# Surcharge de Méthodes en Python

La surcharge de méthodes est un concept clé de la programmation orientée objet (POO) qui permet à une classe de *définir plusieurs méthodes avec le même nom, mais des paramètres différents*. 

En Python, vous pouvez surcharger des méthodes pour personnaliser le comportement en fonction des arguments passés.

## Signature de Méthode

La surcharge de méthodes repose sur la signature de méthode, qui comprend le nom de la méthode et le type, l'ordre ou le nombre de ses paramètres. Deux méthodes doivent avoir une signature différente pour être correctement surchargées.

```python
def nom_de_methode(parametre1, parametre2, ...): # Signature de la méthode
    # Corps de la méthode
```

## Surcharge de Méthodes en Python

En Python, vous pouvez surcharger des méthodes en définissant plusieurs méthodes avec le même nom dans une classe, mais des signatures de paramètres différentes. Lorsqu'une méthode est appelée, Python détermine quelle version de la méthode exécuter en fonction des arguments passés.

```python
class MaClasse:
    def surcharge(self, parametre1):
        # Version avec un seul paramètre
        # Code ici

    def surcharge(self, parametre1, parametre2):
        # Version avec deux paramètres
        # Code ici

# Utilisation de la surcharge de méthodes
objet = MaClasse()
objet.surcharge(arg1)         # Exécute la première version
objet.surcharge(arg1, arg2)   # Exécute la deuxième version
```

Exemple de Surcharge de Méthodes

```python
class Calculatrice:
    def addition(self, a, b):
        return a + b

    def addition(self, a, b, c):
        return a + b + c

# Utilisation de la surcharge de méthodes
calc = Calculatrice()
resultat1 = calc.addition(2, 3)           # Exécute la première version
resultat2 = calc.addition(2, 3, 4)        # Exécute la deuxième version

print(resultat1)  # Affiche 5
print(resultat2)  # Affiche 9
```

## Avantages de la Surcharge de Méthodes

- **Personnalisation du Comportement** : Vous pouvez adapter le comportement d'une méthode en fonction du nombre ou du type de paramètres passés.

- **Lisibilité du Code** : La surcharge de méthodes permet d'avoir des noms de méthodes cohérents pour des opérations similaires.

- **Réutilisation du Code** : Vous pouvez réutiliser le nom de méthode pour effectuer des opérations similaires avec des paramètres différents.

## Exercices Corrigés
**Exercice 1**

Créez une classe Rectangle avec une méthode *aire()* qui accepte deux paramètres, *longueur* et *largeur*, et calcule l'aire du rectangle. 

Ensuite, surchargez la méthode aire() pour qu'elle accepte trois paramètres, longueur, largeur et hauteur, et calcule le volume d'un prisme rectangulaire.

```python
class Rectangle:
    def aire(self, longueur, largeur):
        return longueur * largeur

    def aire(self, longueur, largeur, hauteur):
        return longueur * largeur * hauteur

# Utilisation de la surcharge de méthodes
r = Rectangle()
aire2D = r.aire(5, 3)
aire3D = r.aire(5, 3, 2)

print("Aire 2D :", aire2D)  # Affiche "Aire 2D : 15"
print("Aire 3D :", aire3D)  # Affiche "Aire 3D : 30"
```

**Exercice 2**
Créez une classe Cercle avec une méthode aire() qui accepte un paramètre rayon et calcule l'aire du cercle. Surchargez la méthode aire() pour qu'elle accepte un paramètre diametre et calcule l'aire du cercle en utilisant le diamètre.

```python
class Cercle:
    def aire(self, rayon):
        return 3.14159 * rayon * rayon

    def aire(self, diametre):
        rayon = diametre / 2
        return 3.14159 * rayon * rayon

# Utilisation de la surcharge de méthodes
c = Cercle()
aire1 = c.aire(5)
aire2 = c.aire(10)

print("Aire 1 :", aire1)  # Affiche "Aire 1 : 78.53975"
print("Aire 2 :", aire2)  # Affiche "Aire 2 : 78.53975"
```

