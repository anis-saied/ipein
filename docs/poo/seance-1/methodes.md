---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
date: 01-10-2023
---

# Les méthodes

Les méthodes en Python sont des fonctions associées à des classes et à des objets. Il existe différents types de méthodes, chacun ayant son propre but et utilisation. Comprendre les distinctions entre ces types de méthodes est essentiel pour la programmation orientée objet.

Les méthodes peuvent être classées en trois catégories principales : 

1. les méthodes de classe, 
2. les méthodes d'instance 
3. et les méthodes associés à l'objet après son instanciation. 

## Méthodes d'Instance

Les méthodes d'instance sont des fonctions définies à l'intérieur d'une classe et qui sont appelées sur des objets spécifiques de cette classe. Elles ont automatiquement accès aux attributs de l'objet via le paramètre `self`.

Exemple :

```python

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def presenter(self):
        return "Je m'appelle {} et j'ai {} ans.".format(self.nom, self.age)

# Utilisation des méthodes d'instance
personne1 = Personne("Alice", 30)
print(personne1.presenter())  # Appel de la méthode sur l'objet
```

**Quand utiliser les méthodes d'instance ?**

Utilisez des méthodes d'instance lorsque vous devez effectuer des opérations spécifiques à un objet particulier, en utilisant ses attributs.

## Méthodes de Classe

Les méthodes de classe sont associées à la classe elle-même plutôt qu'à des instances spécifiques de la classe. Elles sont définies à l'intérieur de la classe, mais utilisent généralement le décorateur @classmethod et prennent un premier paramètre de classe, conventionnellement appelé cls.

Exemple :

```python
class Voiture:
    compteur = 0
    
    def __init__(self, marque):
        self.marque = marque
        Voiture.compteur += 1
    
    @classmethod
    def nombre_total(cls):
        return cls.compteur

# Utilisation des méthodes de classe
voiture1 = Voiture("Toyota")
voiture2 = Voiture("Honda")
print(Voiture.nombre_total())  # Appel de la méthode de classe sur la classe
```

**Quand utiliser les méthodes de classe ?** 

Utilisez des méthodes de classe lorsque vous avez besoin d'effectuer des opérations liées à la classe elle-même, mais qui ne dépendent pas spécifiquement des attributs d'une instance.


## Méthodes Statiques

Les méthodes statiques sont des méthodes associées à la classe plutôt qu'à des instances ou à la classe elle-même. Elles sont définies à l'intérieur de la classe, mais utilisent généralement le décorateur @staticmethod. Contrairement aux méthodes de classe, elles ne prennent pas de paramètre de classe (cls) ni de paramètre d'instance (self).

Exemple :

```python

class MathUtil:
    @staticmethod
    def carre(x):
        return x * x

# Utilisation des méthodes statiques
resultat = MathUtil.carre(5)  # Appel de la méthode statique sur la classe
```

Quand utiliser les méthodes statiques : Utilisez des méthodes statiques lorsque vous avez une fonction liée à la classe mais qui ne dépend ni des attributs de l'instance ni de la classe elle-même.
