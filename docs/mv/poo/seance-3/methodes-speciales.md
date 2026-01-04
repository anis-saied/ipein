---
title: Programmation Orientée Objet (POO) en Python
summary: Les Méthodes Spéciales en Python
authors:
  - Anis SAIED
date: 01-10-2023
slug: /informatique/poo/seance-3/methodes-speciales
sidebar_position: 3
last_update:
  date: 2026-01-04
  author: Anis
---

# Les Méthodes Spéciales en Python

Les *méthodes spéciales*, ou *méthodes magiques*, sont des méthodes prédéfinies en Python avec un nom qui commence et se termine par un double souligné (par exemple, `__init__`, `__str__`, `__add__`). 

Elles sont utilisées pour **surcharger** le comportement de base des opérations et des fonctions associées aux objets.

## Méthode `__init__`

La méthode `__init__(self)` est le constructeur de base de tous les objets en Python. Elle est appelée lors de la création d'une instance d'une classe pour effectuer l'initialisation.

Exemple d'utilisation :

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```

## Méthodes `__str__` et `__repr__`
La méthode `__str__(self)` est utilisée pour représenter l'objet sous forme de chaîne de caractères  lorsqu'il est converti en une chaîne (par exemple, avec la fonction `str()` ou lors de l'impression avec `print()`).

La méthode `__repr__(self)` est utilisée pour obtenir une représentation "formelle" de l'objet, généralement utilisée pour le débogage par la fonction `repr()`.

Exemple d'utilisation :
```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return self.nom + " "+ self.age +"ans"

    def __repr__(self):
        return "Personne({}, {})".format(self.nom,self.age)
```

Les méthodes `__str__` et `__repr__`  sont utilisées pour la représentation textuelle d'un objet. Si elles ne sont pas surchargées dans une classe, Python utilise les implémentations par défaut de la classe `object` pour afficher l'objet.

## Méthodes d'Opération Mathématique
Les méthodes spéciales d'opération mathématique permettent de personnaliser le comportement des opérateurs mathématiques tels que l'addition `__add__`, la soustraction `__sub__`, la multiplication `__mul__`, etc.

Exemple d'utilisation :
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

## Méthode `__eq__`

La méthode `__eq__(self,other)` permet de personnaliser la comparaison d'égalité entre deux objets de la classe..

Exemple d'utilisation :
```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age
```

## Méthode `__len__`

La méthode `__len__` permet de personnaliser la manière dont la taille d'un objet est calculée.

Exemple d'utilisation :

Pour une classe de bibliothèque, vous pouvez surcharger la méthode `__len__` pour renvoyer le nombre total de livres disponibles dans cette bibliothèque. 

```python
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def __len__(self):
        return len(self.livres)

# Créez une instance de la classe Bibliotheque
ma_bibliotheque = Bibliotheque()

# Ajoutez des livres à la bibliothèque
livre1 = Livre("L'Alchimiste", "Paulo Coelho")
livre2 = Livre("1984", "George Orwell")
livre3 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")

ma_bibliotheque.ajouter_livre(livre1)
ma_bibliotheque.ajouter_livre(livre2)
ma_bibliotheque.ajouter_livre(livre3)

# Utilisation de la méthode __len__ pour obtenir le nombre de livres dans la bibliothèque
nombre_de_livres = len(ma_bibliotheque)

print("Nombre de livres dans la bibliothèque :", nombre_de_livres)
```


## Exercices

1. Créez une classe *Vecteur* qui représente des vecteurs en 2D avec des attributs x et y. La classe doit avoir une méthode spéciale `__abs__` pour calculer la norme du vecteur.

Rappel : La fonction `abs()` appliquée à un vecteur en mathématiques (en particulier en géométrie) renvoie la norme du vecteur. La norme d'un vecteur est une mesure de sa longueur, c'est-à-dire la distance du point de départ (origine) au point d'extrémité (bout de la flèche) du vecteur.

Pour un vecteur bidimensionnel (x, y), la formule est la suivante :

`Norme = √(x^2 + y^2)`

Pour un vecteur tridimensionnel (x, y, z), la formule est étendue comme suit :

`Norme = √(x^2 + y^2 + z^2)`

**Solution**
```python
import math

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

# Exemple d'utilisation
v = Vecteur(3, 4)
norme = abs(v)

print("Norme du vecteur :",norme)
```


## Conclusion

Les méthodes spéciales en Python permettent de personnaliser le comportement des objets de vos classes. Elles facilitent l'interaction avec ces objets et rendent votre code plus lisible et plus propre. En les utilisant correctement, vous pouvez concevoir des classes plus expressives et puissantes.
