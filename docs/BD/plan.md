---
title: Bases de Données, Algèbre Relationnelle et SQLite en Python
summary: Introduction aux bases de données, à l'algèbre relationnelle et à l'utilisation de SQLite en Python
authors:
  - ANIS SAIED
date: 23-01-2024
---

# Introduction aux Bases de Données, Algèbre Relationnelle et SQLite en Python

## Objectif de ce chapitre

Ce chapitre vise à introduire les concepts fondamentaux des bases de données, de l'algèbre relationnelle, et à expliquer comment utiliser SQLite en Python. Nous explorerons la création de bases de données, les requêtes SQL, et la manipulation de données à l'aide de SQLite dans l'environnement Python.

## Contenu du Cours

Le cours sur les bases de données, l'algèbre relationnelle et SQLite sera divisé en trois parties, chacune couvrant un aspect essentiel de la gestion des données.

###### Partie 1 : Introduction aux Bases de Données et à l'Algèbre Relationnelle

[Introduction aux Bases de Données.pdf](./intro_BD.pdf)

[Cours Algèbre Relationnelle.pdf](./AR.pdf)

Corrigé des exercices du cours :

- [Corrigé AR.pdf](./AR-corrige.pdf)

###### Partie 2 : Transition de l'Algèbre Relationnelle au langage SQL

1. [Cours de l'Algèbre relationnelle à SQL.pdf](./AR-SQL.pdf)

Corrigé des exercices du cours :

- [Corrigé AR-SQL.pdf](./AR-SQL-corrige.pdf)

###### Partie 3 : Requêtes SQL Avancées et utilisation de SQLite en Python

1. [SQL-SQLite.pdf](./SQL-SQLite.pdf)
1. [Requete Select.pdf](./Requete-Select.pdf)

Corrigé des exercices du cours :

- [Corrigé SQL-SQLite.pdf](./SQL-SQLite-corrige.pdf)
- [Exemple d'utilisation de SQL avec SQLite-Python.py](./employes.py)



Vous pouvez manipuler une base données SQLite avec l'outil [**DB Browser For SQLite**](http://sqlitebrowser.org) de deux manières

**Méthode 1**: Utiliser le fichier de base de données d'extension **.db** qui contient les tables créées et remplies.

- Télécharger le fichier [employes.db](./employes.db)
- Lancer l'outil DB Browser For Sqlite
  - Menu File / open Database
  - choisir le fichier employes.db
- Ouvrir l'anglet "Execute SQL" et commencer à taper et tester des commandes SQL.



**Méthode 2**: Créer vous-même la base de données, créer les tables et les remplir.

- Télécharger le fichier [employes.sql](./employes.sql)
- Ouvrir le logiciel BD Browser for SQLite 
- Créer une nouvelle base de données: 
  - Menu File / New DataBase
  - tapez le nom de la base de données, par exemple: *ma_base.db*
  - Une fenêtre s'ouvre automatiquement pour créer la première table, Fermez la.

- Ouvrir l'anglet "Execute SQL" 
  - Copier/coller le contenu de fichier **employes.sql** dans la zone de texte reservée à la création du code SQL. 
  - Cliquez sur la flèche pour exécuter ce code SQL permettant ainsi de créer toutes les tables et les remplir.



Vous pouvez maintenant essayer les requêtes SQL vues en classe et répondre à d'autres questions que vous imaginez.

