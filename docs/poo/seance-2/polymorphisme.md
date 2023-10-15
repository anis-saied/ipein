---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
date: 01-10-2023
---

# Le Polymorphisme en Python

Le polymorphisme est l'un des principes fondamentaux de la programmation orientée objet (POO) qui permet à des objets de différentes classes d'être traités de manière uniforme. 

Cela signifie que vous pouvez utiliser des méthodes ou des opérateurs sur ces objets sans vous soucier de leur type spécifique. En Python, le polymorphisme est largement pris en charge grâce à la flexibilité du langage.

## Comprendre le Polymorphisme

Le polymorphisme peut être divisé en deux types principaux : le polymorphisme de méthode et le polymorphisme d'opérateur.

## Polymorphisme de Méthode

Le polymorphisme de méthode vous permet d'appeler une méthode sur un objet, et *la méthode exécutée dépend du type de cet objet*. Par exemple, supposons que nous ayons deux classes, `Chien` et `Chat`, chacune ayant une méthode `crier` :

```python
class Chien:
    def crier(self):
        return "Woof!"

class Chat:
    def crier(self):
        return "Miaou!"
```
Maintenant, nous pouvons créer des objets de ces classes et appeler la méthode crier :
```python
chien = Chien()
chat = Chat()

animaux = [chien, chat]

for animal in animaux:
    print(animal.crier())
```
Lorsque nous appelons crier sur chaque objet, la méthode appropriée est appelée en fonction du type de l'objet.

## Polymorphisme d'Opérateur

Le polymorphisme d'opérateur permet d'utiliser des opérateurs sur des objets de différentes classes. 

Par exemple, vous pouvez utiliser l'opérateur ` + ` pour concaténer des chaînes de caractères, mais aussi pour ajouter des nombres :

```python
a = 5
b = 10
resultat = a + b
print(resultat)  # Affiche 15

chaine1 = "Hello, "
chaine2 = "world!"
resultat = chaine1 + chaine2
print(resultat)  # Affiche "Hello, world!"
```

Python permet d'utiliser de nombreux opérateurs de cette manière, tant que les classes définissent les méthodes spéciales appropriées, comme `__add__`, `__sub__`, etc.


## Avantages du Polymorphisme

Le polymorphisme présente plusieurs avantages :

- **Flexibilité**: Vous pouvez traiter différents objets de manière uniforme, ce qui simplifie le code.

Exemple :
```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def faire_crier(self):
        pass

class Chien(Animal):
    def faire_crier(self):
        return "Woof!"

class Chat(Animal):
    def faire_crier(self):
        return "Miaou!"

# Utilisation de la flexibilité du polymorphisme
def faire_crier_et_afficher(animal):
    print("{} fait {}".format(animal.nom, animal.faire_crier()))

animaux = [Chien("Rex"), Chat("Whiskers")]

for animal in animaux:
    faire_crier_et_afficher(animal)
```
Dans cet exemple, nous utilisons le polymorphisme pour appeler la méthode *faire_crier* sur des objets de différentes classes, ce qui permet à chaque animal de faire le bruit approprié.

- **Réutilisation du Code** : Vous pouvez réutiliser des méthodes ou des opérateurs sur des objets de différentes classes.

Exemple : 
```python
class Forme:
    def aire(self):
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return 3.14159265359 * self.rayon * self.rayon

class Rectangle(Forme):
    def __init(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

# Utilisation de la réutilisation du code via le polymorphisme
cercle = Cercle(5)
rectangle = Rectangle(4, 6)

formes = [cercle, rectangle]

for forme in formes:
    print(f"L'aire de la forme est {forme.*aire()*}")
```


- **Extension Facile**: Vous pouvez étendre le polymorphisme pour prendre en charge de nouvelles classes sans modifier le code existant.

Exemple :
```python
# Nouvelle classe Triangle
class Triangle(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur

triangle = Triangle(3, 4)

# Sans modifier le code existant, nous pouvons ajouter un triangle à la liste des formes
formes.append(triangle)

for forme in formes:
    print(f"L'aire de la forme est {forme.*aire()*}")
```

## Exercices
**Exercice 1** : Calcul d'aire de formes géométriques

1. Écrivez une classe de base appelée Forme avec une méthode *aire()*.
2. Ensuite, créez trois sous-classes de Forme : *Cercle*, *Rectangle*, et *Triangle*, chacune avec sa propre implémentation de la méthode *aire()*.
3. Enfin, créez une liste de formes contenant des instances de ces trois sous-classes.
4. Calculez et affichez l'aire de chaque forme à partir de la liste.

**Solution**
```python
class Forme():
    def aire(self):
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return 3.14159265359 * self.rayon * self.rayon

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

class Triangle(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur

# Création d'une liste de formes
formes = [Cercle(5), Rectangle(4, 6), Triangle(3, 4)]

# Calcul et affichage de l'aire de chaque forme
for forme in formes:
    print("L'aire de la forme est "+str(forme.aire()))

# Résultat attendu :
# L'aire du cercle est 78.53981633974483
# L'aire du rectangle est 24
# L'aire du triangle est 6.0
```

**Exercice 2** : Polymorphisme avec des véhicules

1. Créez une classe de base appelée *Vehicule* avec une méthode *afficher_info* qui affiche des informations de base sur le véhicule, telles que le nom du véhicule.

2. Créez trois sous-classes de Vehicule : *Voiture*, *Moto*, et *Velo*, chacune avec son propre constructeur et des informations spécifiques (par exemple, le nombre de roues pour chaque type de véhicule).

3. Instanciez plusieurs véhicules de chaque type (voiture, moto, vélo) et stockez-les dans une liste.

4. Utilisez le polymorphisme pour appeler la méthode *afficher_info* pour chaque véhicule de la liste, affichant ainsi des informations spécifiques à chaque type de véhicule.

**Solution**
```python
class Vehicule:
    def __init__(self, nom):
        self.nom = nom

    def afficher_info(self):
        print("Véhicule : {}".format(self.nom))

class Voiture(Vehicule):
    def __init__(self, nom, roues):
        super().__init__(nom)
        self.roues = roues

    def afficher_info(self):
        print("Voiture : {}, Roues : {}".format(self.nom, self.roues))

class Moto(Vehicule):
    def __init__(self, nom, roues):
        super().__init__(nom)
        self.roues = roues

    def afficher_info(self):
        print("Moto : {}, Roues : {}".format(self.nom, self.roues))

class Velo(Vehicule):
    def __init__(self, nom, roues):
        super().__init__(nom)
        self.roues = roues

    def afficher_info(self):
        print("Vélo : {}, Roues : {}".format(self.nom, self.roues))

# Création d'une liste de véhicules
vehicules = [Voiture("Sedan", 4), Moto("Sportive", 2), Velo("Montagne", 2), Voiture("Compacte", 4)]

# Utilisation du polymorphisme pour afficher les informations de chaque véhicule
for vehicule in vehicules:
    vehicule.afficher_info()
```