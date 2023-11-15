---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
date: 09-10-2023
---


# Les Constructeurs et Destructeurs en Python

En Python, les constructeurs et les destructeurs sont des méthodes spéciales qui sont utilisées pour initialiser et libérer des ressources associées à un objet. Ils sont couramment utilisés dans la programmation orientée objet pour personnaliser le comportement des classes.

## Le Constructeur `__init__`

Le constructeur est une méthode spéciale appelée automatiquement lors de la création d'un objet à partir d'une classe. Il est utilisé pour initialiser les attributs de l'objet et effectuer d'autres opérations d'initialisation. Le nom de la méthode doit être `__init__`.

Exemple de constructeur :

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```
Dans cet exemple, le constructeur `__init__` prend deux paramètres (**self**, qui fait référence à l'objet lui-même, ainsi que nom et age) et initialise les attributs nom et age de l'objet.

## Le Destructeur `__del__`

Le destructeur est une autre méthode spéciale appelée automatiquement lorsque l'objet n'a plus de références et doit être détruit. Il est utilisé pour effectuer des opérations de nettoyage ou de libération de ressources. Le nom de la méthode doit être `__del__`.

Exemple de destructeur (à titre d'illustration) :

```python
class Fichier:
    def __init__(self, nom):
        self.nom = nom
        print("Le fichier " + self.nom + " a été créé.")
    
    def __del__(self):
        print("Le fichier " + self.nom + " a été supprimé")

f = Fichier("mon_fichier.txt")
print(f.nom)
# A la fin du script toutes les instances sont détruites (via __del__)
```

Dans cet exemple, le destructeur `__del__` imprime un message lorsque l'objet de la classe Fichier est détruit.

## Utilisation des Constructeurs et Destructeurs

Les constructeurs sont utilisés pour initialiser les attributs de l'objet lors de sa création, tandis que les destructeurs sont utilisés pour effectuer des opérations de nettoyage lorsque l'objet n'est plus nécessaire. Les destructeurs ne sont pas toujours nécessaires, car Python gère automatiquement la gestion de la mémoire, mais ils peuvent être utiles pour libérer des ressources externes.

```python
# Utilisation des constructeurs
personne = Personne("Alice", 30)

# Utilisation des destructeurs (à titre d'illustration)
fichier = Fichier("mon_fichier.txt")
del fichier  # Appel du destructeur pour libérer la ressource
```

Les constructeurs et destructeurs sont des outils puissants pour personnaliser le comportement des classes en Python, en leur permettant d'effectuer des opérations d'initialisation et de nettoyage spécifiques.
<hr>
En résumé, le constructeur `__init__` est utilisé pour initialiser les attributs de l'objet lors de sa création, tandis que le destructeur `__del__` est utilisé pour effectuer des opérations de nettoyage lorsque l'objet est détruit. Ces méthodes spéciales sont couramment utilisées en programmation orientée objet en Python.