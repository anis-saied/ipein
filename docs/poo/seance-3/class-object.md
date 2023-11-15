---
title: Programmation Orientée Objet (POO) en Python
summary: La Classe Object en Python et ses Méthodes Spéciales
authors:
  - Anis SAIED
date: 25-10-2023
---

# La Classe Object en Python et ses Méthodes Spéciales

La classe **object** est la classe de base de toutes les classes en Python. Elle est *implicitement héritée* par toutes les classes définies dans Python. 

La classe object est au sommet de la hiérarchie de l'héritage des classes, ce qui signifie que toutes les autres classes, même si elles n'en héritent pas explicitement, sont en fin de compte des sous-classes de la classe object. 

La classe object définit certaines méthodes spéciales et attributs prédéfinis qui sont hérités par toutes les autres classes.

Les principales méthodes spéciales définies dans la classe object incluent :

- `__init__(self)`: Cette méthode est le constructeur de base de tous les objets en Python. Elle est appelée lors de la création d'une instance d'une classe pour effectuer l'initialisation.

- `__str__(self)`: Cette méthode est utilisée pour représenter l'objet sous forme de chaîne de caractères lorsqu'il est converti en une chaîne (par exemple, avec la fonction `str()` ou lors de l'impression avec la fonction `print()`).

- `__repr__(self)`: Cette méthode est utilisée pour obtenir une représentation "formelle" de l'objet, généralement sous forme de chaîne de caractères. Elle est utilisée par la fonction `repr()`.

- `__eq__(self, other)`: Cette méthode est utilisée pour définir l'égalité entre deux objets de la classe. Elle est appelée lorsque l'on compare des objets avec l'opérateur `==`.


Pour connaître les méthodes et les attributs prédéfinis de la classe object, vous pouvez utiliser la fonction `dir()` en Python. Voici comment vous pouvez l'utiliser : `print(dir(object))`

Cela affichera une liste de toutes les méthodes et attributs disponibles dans la classe object. 

Les *méthodes spéciales* de la classe *object* peuvent être **surchargées** (redéfinies) dans les classes dérivées pour personnaliser le comportement des objets de ces classes.

La documentation officielle de Python contient des informations utiles sur la [classe object](https://docs.python.org/3/library/functions.html?highlight=object#object).

Le code source la classe `object` codé en langage C [cpython/Objects/object.c at main · python/cpython · GitHub](https://github.com/python/cpython/blob/main/Objects/object.c)


<hr>
La classe object elle-même est conçue pour être une classe de base minimale, et son but principal est de fournir l'héritage de base et les méthodes spéciales communes à toutes les autres classes en Python.

L'utilisation la plus courante de la classe object est implicitement lors de la définition de classes dérivées. Toutes les classes en Python héritent automatiquement de la classe object, même si ce n'est pas spécifiquement déclaré. Par exemple :

```python
class MaClasse:
    pass

# MaClasse hérite de la classe object
my_instance = MaClasse()
```
Dans cet exemple, *MaClasse* hérite de la classe *object*, ce qui signifie que *my_instance* est une instance de *MaClasse*, mais elle hérite également des fonctionnalités de base de la classe *object*.