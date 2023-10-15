---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
---

# TP1 POO : Syntaxe de Base de la POO en Python

## Création de classes et d'objets

**Exercice 1 :** Créer une classe simple

Créez une classe Personne avec un attribut nom. Instanciez un objet de cette classe et affichez le nom de la personne.

## Attributs

**Exercice 2 :** Créer une classe pour les voitures

Créez une classe Voiture avec les attributs marque et annee. Instanciez plusieurs objets de cette classe avec différentes marques et années et affichez les informations sur chaque voiture.

## Méthodes

**Exercice 3 :** Ajouter des méthodes

Ajoutez une méthode **afficher_info()** à la classe Voiture qui affiche les informations de la voiture. Appelez cette méthode pour chaque objet de la classe Voiture que vous avez créé dans l'exercice précédent.

## Constructeurs et destructeurs

**Exercice 4 :** Créer un constructeur paramétrable

Ajouter des paramètres au constructeur (`__init__`) de la classe Voiture pour initialiser les attributs marque et annee lors de la création de l'objet.

**Exercice 5 :** Ajouter un destructeur

Ajoutez un destructeur (`__del__`) à la classe Voiture qui affiche un message lorsque la voiture est détruite.

**Exercice 6 :** Nettoyage des ressources

Utilisez le destructeur pour simuler la libération de ressources associées à une voiture (par exemple, fermez une connexion à un fichier text). Affichez un message approprié lorsque la voiture est détruite.

<hr>

Ce TP couvre les concepts de base de la POO en Python, de l'introduction aux classes et aux objets jusqu'à la création de constructeurs et de destructeurs. Vous pouvez progresser à votre propre rythme en résolvant chaque exercice.