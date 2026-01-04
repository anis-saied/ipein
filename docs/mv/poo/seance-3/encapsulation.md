---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
date: 01-10-2023
slug: /informatique/poo/seance-3/encapsulation
sidebar_position: 2
last_update:
  date: 2026-01-04
  author: Anis
---

# L'Encapsulation en Python

L'encapsulation est l'un des concepts clés de la programmation orientée objet (POO). Il s'agit du mécanisme qui permet de restreindre l'accès aux détails internes d'une classe tout en exposant une interface publique pour interagir avec cette classe. 

En Python, l'encapsulation repose principalement sur la convention plutôt que sur la stricte application de restrictions d'accès.

## Attributs et Méthodes
### Attributs
Les attributs sont des variables associées à une classe. Ils peuvent être utilisés pour stocker des données spécifiques à cette classe.

En Python, il y a trois types d'attributs :

1. **Attributs Publics** : Ils sont *accessibles* directement depuis n'importe où.
2. **Attributs Protégés** : Ils commencent par un seul souligné (par exemple, `_attribut`). Bien qu'ils soient accessibles depuis l'extérieur de la classe, ils sont considérés comme des attributs "protégés", et il est *recommandé* de ne pas y accéder directement.
3. **Attributs Privés**: Ils commencent par deux soulignés (par exemple, `__attribut`). Ils sont destinés à être privés et *ne devraient pas* être accessibles depuis l'extérieur de la classe.

### Méthodes

Les méthodes sont des fonctions associées à une classe. Elles définissent le comportement de la classe.

De la même manière, il existe trois types de méthodes :

1. **Méthodes Publiques** : Elles sont accessibles depuis n'importe où.
2. **Méthodes Protégées** : Elles commencent par un seul souligné (par exemple, `_methode`). Bien qu'elles soient accessibles depuis l'extérieur de la classe, elles sont considérées comme des méthodes "protégées".
3. **Méthodes Privées** : Elles commencent par deux soulignés (par exemple, `__methode`). Elles sont destinées à être privées et ne devraient pas être accessibles depuis l'extérieur de la classe.

## Encapsulation en Python

En Python, l'encapsulation repose sur des **conventions** plutôt que sur des mécanismes stricts de restriction d'accès. Voici quelques pratiques courantes d'encapsulation en Python :

1. **Attributs Protégés** : Utilisez des attributs commençant par un seul souligné (par exemple, _attribut) pour indiquer qu'ils sont destinés à être "protégés", mais laissez-les accessibles depuis l'extérieur de la classe.

2. **Attributs Privés** : Utilisez des attributs commençant par deux soulignés (par exemple, __attribut) pour indiquer qu'ils sont privés. Cela les rend plus difficiles à accéder depuis l'extérieur de la classe, mais ils ne sont pas totalement inaccessibles.

3. **Méthodes Privées** : Les méthodes privées commençant par deux soulignés (par exemple, __methode) ne sont pas accessibles directement depuis l'extérieur de la classe. Cependant, elles peuvent être appelées depuis d'autres méthodes de la classe.

### Exemple d'Encapsulation

```python
class CompteBancaire:
    def __init__(self, solde):
        self.__solde = solde  # Attribut privé

    def deposer(self, montant):
        self.__solde += montant

    def retirer(self, montant):
        if self.__solde >= montant:
            self.__solde -= montant
        else:
            print("Fonds insuffisants")

    # Méthode d'accès (getter) pour l'attribut privé
    def solde(self):
        return self.__solde

    def __str__(self):
        return "Solde actuel :"+ str(self.__solde)

# Exemple d'utilisation
compte = CompteBancaire(1000)
compte.deposer(500)
compte.retirer(200)
print(compte)
```

Dans cet exemple, la classe CompteBancaire utilise l'encapsulation pour masquer l'attribut privé `__solde` et expose une méthode d'accès (`solde`) pour obtenir la valeur de cet attribut. 
 
L'encapsulation permet de contrôler l'accès aux données internes de la classe et fournit une interface publique pour interagir avec l'objet compte.

