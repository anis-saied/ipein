---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
date: 01-10-2023
---

# Les attributs
Python prend en charge plusieurs types d'attributs, qui sont des variables associées à des classes et à des objets. Chacun de ces types d'attributs a des caractéristiques distinctes et est utilisé dans des contextes différents.

Les attributs peuvent être classés en trois catégories principales : 

1. les attributs de classe, 
2. les attributs d'instance 
3. et les attributs associés à l'objet après son instanciation. 

## Attributs de Classe

Les attributs de classe sont partagés par toutes les instances (objets) de la classe. Ils sont définis à l'intérieur de la classe, en dehors des méthodes, et ne sont pas liés à une instance spécifique. 

Les attributs de classe sont généralement utilisés pour stocker des informations qui sont partagées par toutes les instances de la classe.

Exemple :
```python
class Compteur:
    count = 0  # Attribut de classe
    
    def __init__(self):
        Compteur.count += 1  # Incrémente l'attribut de classe 
                             # lors de la création d'une instance

# Utilisation des attributs de classe
objet1 = Compteur()
print(Compteur.count)  # Affiche 1
objet2 = Compteur()
print(Compteur.count)  # Affiche 2
```

**Quand utiliser les attributs de classe ?**

Utilisez des attributs de classe lorsque vous avez besoin de stocker des données qui sont partagées par toutes les instances de la classe, comme un compteur global.

## Attributs d'Instance
Les attributs d'instance sont spécifiques à chaque instance de la classe. Chaque objet a sa propre copie des attributs d'instance. Ils sont généralement définis dans le constructeur de la classe (`__init__`) en utilisant le préfixe `self`. Les attributs d'instance sont utilisés pour stocker des données spécifiques à chaque objet.

Exemple :

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom  # Attribut d'instance
        self.age = age  # Attribut d'instance

# Utilisation des attributs d'instance
personne1 = Personne("Alice", 30)
print(personne1.nom)  # Affiche "Alice"
print(personne1.age)  # Affiche 30

personne2 = Personne("Bob", 25)
print(personne2.nom)  # Affiche "Bob"
print(personne2.age)  # Affiche 25
```

**Quand utiliser les attributs d'instance ?**

Utilisez des attributs d'instance lorsque vous devez stocker des données spécifiques à chaque objet, telles que les caractéristiques individuelles d'une personne.

## Attributs Associés à l'Objet après son Instanciation

En Python, vous pouvez ajouter des attributs à un objet après son instanciation. Ces attributs ne sont pas définis dans la classe ou le constructeur, mais ils sont attachés à l'objet à la volée. 

Cette flexibilité est utile lorsque vous avez besoin d'ajouter des données à un objet de manière dynamique.

Exemple :
```python

class Livre:
    def __init__(self, titre):
        self.titre = titre

# Création d'un objet
livre1 = Livre("Python pour les Débutants")

# Ajout d'un attribut associé à l'objet après son instanciation
livre1.auteur = "John Doe"

# Utilisation de l'attribut associé à l'objet
print(livre1.auteur)  # Affiche "John Doe"
```

**Quand utiliser les attributs associés à l'objet ?** 

Utilisez des attributs associés à l'objet lorsque vous devez ajouter des données à un objet après son instanciation. Cela peut être pratique pour personnaliser des objets individuellement.



<hr>
En résumé, les attributs de classe sont partagés par toutes les instances, les attributs d'instance sont spécifiques à chaque objet, et les attributs associés à l'objet permettent d'ajouter des données dynamiquement. Choisissez le type d'attribut qui correspond le mieux à vos besoins en fonction du contexte de votre programme.