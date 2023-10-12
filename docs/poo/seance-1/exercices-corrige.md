---
title: Programmation Orientée Objet (POO) en Python
summary: Introduction à la Programmation Orientée Objet (POO) en Python
authors:
  - Anis SAIED
---

# TP1 POO  : Syntaxe de Base de la POO en Python ~ Corrigé

**Exercice 1 :** Créer une classe simple

```python
class Personne:
    def __init__(self, nom):
        self.nom = nom

# Instanciation d'un objet de la classe Personne
personne1 = Personne("Alice")

# Affichage du nom de la personne
print("Nom de la personne :", personne1.nom)
```

**Exercice 2 :** Créer une classe pour les voitures

```python
class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee

# Instanciation de plusieurs objets de la classe Voiture
voiture1 = Voiture("Toyota", 2020)
voiture2 = Voiture("Honda", 2022)

# Affichage des informations sur chaque voiture
print("Voiture 1 - Marque :", voiture1.marque, "Année :", voiture1.annee)
print("Voiture 2 - Marque :", voiture2.marque, "Année :", voiture2.annee)
```

**Exercice 3 :** Ajouter des méthodes

```python
class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee

    def afficher_info(self):
        print("Marque :", self.marque)
        print("Année :", self.annee)

# Instanciation de plusieurs objets de la classe Voiture
voiture1 = Voiture("Toyota", 2020)
voiture2 = Voiture("Honda", 2022)

# Appel de la méthode afficher_info pour chaque voiture
print("Informations sur la voiture 1 :")
voiture1.afficher_info()
print("Informations sur la voiture 2 :")
voiture2.afficher_info()
```

**Exercice 4 :** Créer un constructeur paramétrable

```python
class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee

# Instanciation d'un objet de la classe Voiture avec des paramètres
voiture = Voiture("Toyota", 2020)

# Affichage des informations sur la voiture
print("Marque :", voiture.marque)
print("Année :", voiture.annee)
```

**Exercice 5 :** Ajouter un destructeur

```python
class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee

    def __del__(self):
        print(f"La voiture de marque {self.marque} a été détruite")

# Instanciation d'un objet de la classe Voiture
voiture = Voiture("Toyota", 2020)

# Suppression de la référence à l'objet pour déclencher le destructeur
del voiture
```

**Exercice 6 :** Nettoyage des ressources

```python
class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee

    def __del__(self):
        print(f"La voiture de marque {self.marque} de {self.annee} a été détruite")

    def fermer_connexion(self):
        print(f"Connexion fermée pour la voiture de marque {self.marque}")

# Instanciation d'un objet de la classe Voiture
voiture = Voiture("Toyota", 2020)

# Utilisation du destructeur pour simuler la fermeture de la connexion
voiture.fermer_connexion()  # Simule la fermeture d'une connexion
del voiture
```
