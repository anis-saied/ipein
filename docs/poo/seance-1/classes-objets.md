---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
---

# Syntaxe de Base de la POO en Python

## Introduction aux classes et aux objets

Dans cette première séance, nous aborderons les concepts de base de la programmation orientée objet en Python. Commençons par comprendre ce que sont les classes et les objets.

### Les classes

Une classe est un modèle ou un plan pour créer des objets. Elle définit les attributs (variables) et les méthodes (fonctions) que les objets de cette classe auront. En Python, vous pouvez créer une classe en utilisant le mot-clé `class`.

Exemple de définition d'une classe simple :

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```

### Les objets

Un objet est une instance d'une classe. C'est une entité concrète qui possède des attributs et peut exécuter des méthodes. Pour créer un objet à partir d'une classe, vous appelez le constructeur de la classe en utilisant la notation **nom_de_classe()**.

Exemple de création d'un objet à partir de la classe *Personne* :

```python
personne1 = Personne("Ahmed", 30)
personne2 = Personne("Sami", 25)
```

## Création de classes et d'objets

Maintenant que nous comprenons ce que sont les classes et les objets, passons à la création pratique de classes et d'objets en Python.

### Définition d'une classe

Pour définir une classe, utilisez le mot-clé `class`, suivi du nom de la classe (en utilisant la convention *CamelCase*) et du signe ` : `. 

À l'intérieur de la classe, vous définirez les attributs et les méthodes.

Exemple de définition de classe :

```python
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
```

### Création d'objets

Pour créer un objet à partir d'une classe, appelez le constructeur de la classe en utilisant la notation `nom_de_classe()`. Vous pouvez passer des arguments au constructeur pour initialiser les attributs de l'objet.

Exemple de création d'objets à partir de la classe Voiture :

```python
voiture1 = Voiture("Toyota", "Camry")
voiture2 = Voiture("Honda", "Civic")
```

### Accès aux attributs

Vous pouvez accéder aux attributs d'un objet en utilisant la notation point `objet.attribut`. 

Par exemple :

```python
print(voiture1.marque)  # Affiche "Toyota"
print(voiture2.modele)  # Affiche "Civic"
```

### Utilisation de méthodes

Les méthodes sont des fonctions définies à l'intérieur de la classe et peuvent être appelées sur les objets de cette classe. Elles sont utiles pour effectuer des opérations spécifiques sur les objets.

Exemple de méthode dans la classe Voiture :

```python
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def description(self):
        return "{} {}".format(self.marque, self.modele)
```

Utilisation de la méthode description :

```python
voiture1 = Voiture("Toyota", "Camry")
print(voiture1.description())  # Affiche "Toyota Camry"
```

Dans cette première partie, nous avons exploré la création de classes et d'objets en Python, ainsi que l'accès aux attributs et l'utilisation de méthodes. Dans les parties suivantes, nous approfondirons d'autres aspects de la programmation orientée objet.
