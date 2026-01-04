---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
date: 01-10-2023
slug: /informatique/poo/seance-1/methodes
sidebar_position: 6
last_update:
  date: 2026-01-04
  author: Anis
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

