---
title: Programmation Orientée Objet (POO) en Python
summary: Héritage (POO) en Python
authors:
  - Anis SAIED
date: 15-10-2023
slug: /informatique/poo/seance-2/heritage
sidebar_position: 3
last_update:
  date: 2026-01-04
  author: Anis
---

# Héritage de classes

## Introduction
L'héritage est une caractéristique fondamentale de la programmation orientée objet en Python, permettant de créer de nouvelles classes en se basant sur des classes existantes.

L'héritage offre la possibilité de créer une classe enfant qui hérite des attributs et des méthodes d'une classe parente. Ce concept favorise la réutilisation du code et la structuration des classes en hiérarchies.

## Syntaxe de l'héritage
En Python, l'héritage s'effectue en spécifiant la classe parente entre parenthèses lors de la définition de la classe enfant. Par exemple :
```python
class Enfant(Parent):
    # Attributs et méthodes spécifiques à la classe enfant
```

## Exemple d'héritage
Pour illustrer l'héritage, nous allons créer une classe "Animal" qui servira de classe parente, puis une classe "Chien" qui héritera des caractéristiques de la classe "Animal."
```python
# Création de la classe parente "Animal"
class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def afficher_info(self):
        print(self.nom + " est un " + self.espece)

# Création de la classe enfant "Chien" en utilisant l'héritage
class Chien(Animal):
    def __init__(self, nom, race):
        # Appel du constructeur de la classe parente
        super().__init__(nom, espece="chien")
        self.race = race

    # Redéfinition de la méthode afficher_info
    def afficher_info(self):
        print(self.nom + " est un chien de race " + self.race)

# Création d'objets des classes Animal et Chien
animal1 = Animal("Rex", "chien")
chien1 = Chien("Buddy", "Labrador")

# Appel de la méthode afficher_info de chaque objet
animal1.afficher_info()  # Affiche "Rex est un chien"
chien1.afficher_info()    # Affiche "Buddy est un chien de race Labrador"
```
Dans cet exemple, nous avons créé une classe parente "Animal" avec des attributs "nom" et "espèce" ainsi qu'une méthode "afficher_info". 

Ensuite, nous avons défini une classe enfant "Chien" en utilisant l'héritage de la classe "Animal". 

La classe "Chien" a son propre attribut "race" et redéfinit la méthode "afficher_info" pour afficher des informations spécifiques aux chiens. 

Enfin, nous avons créé des objets des deux classes et appelé la méthode "afficher_info" pour chaque objet.

## Les avantages 
Les principaux avantages de l'héritage en programmation orientée objet (POO) en Python sont les suivants :

- **Avantage 1 : Réutilisation du code** : L'héritage permet de *réutiliser les attributs et méthodes* d'une classe parente dans une classe enfant, **évitant ainsi la duplication de code**.

- **Avantage 2 : Création de hiérarchies de classes** : Vous pouvez créer une *structure hiérarchique* de classes, où chaque classe enfant hérite des fonctionnalités de la classe parente. Par exemple, une classe "Véhicule" peut être la classe parente de "Voiture" et "Moto".

- **Avantage 3 : Extensibilité** : Vous pouvez ajouter de nouvelles *fonctionnalités spécifiques à une classe enfant* tout en conservant les fonctionnalités héritées de la classe parente.

- **Avantage 4 : Modification centralisée** : Si vous devez apporter des modifications à une *fonctionnalité partagée* par plusieurs classes, vous pouvez le faire dans la classe parente, ce qui affectera automatiquement toutes les classes enfant.

- **Avantage 5 : Développement plus rapide** : L'héritage accélère le développement en *réduisant la quantité de code* que vous devez écrire pour créer de nouvelles classes.

Exemple :
```python
# Classe parente "Animal"
class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def afficher_info(self):
        print(self.nom + " est un " + self.espece)

# Classe enfant "Chien" héritant d'Animal
class Chien(Animal):
    def __init__(self, nom, race):
        super().__init__(nom, espece="chien")
        self.race = race

    def aboyer(self):
        print(self.nom + " aboie")

# Sous-classe de Chien : ChienDomestique
class ChienDomestique(Chien):
    def __init__(self, nom, race, proprietaire):
        super().__init__(nom, race)
        self.proprietaire = proprietaire

    def saluer_proprietaire(self):
        print(self.nom + " salue son propriétaire " + self.proprietaire)


# Utilisation de l'héritage
animal1 = Animal("Rex", "chien")
animal1.afficher_info()  # Affiche "Rex est un chien"

chien1 = Chien("Buddy", "Labrador")

chien1.afficher_info()  # Affiche "Buddy est un chien"
chien1.aboyer()         # Avantage 3 : Extensibilité
                        # Affiche "Buddy aboie"

chien2 = ChienDomestique("Fido", "Terrier", "Alice")
chien2.afficher_info()
chien2.saluer_proprietaire()
```
Dans le code prédendent, grâce à l'héritage, on a pu appliquer :

1. La **Réutilisation du code** : La classe *Chien* réutilise le constructeur (`__init__`) de la classe parente *Animal*. Cela permet de ne pas avoir à réécrire le code pour initialiser les attributs *nom* et *espece* dans *Chien*.

2. La **Création de hiérarchies de classes** : L'avantage de la création de hiérarchies de classes peut être illustré par la possibilité de créer des classes enfant supplémentaires qui partagent des caractéristiques communes avec la classe parente. Dans cet exemple, nous avons la classe *ChienDomestique* qui hérite de la classe *Chien*, qui à son tour hérite de la classe *Animal*. La classe *ChienDomestique* ajoute un attribut *proprietaire* et une méthode *saluer_proprietaire*, illustrant la hiérarchie d'héritage.

3. L'**Extensibilité** : En utilisant l'héritage, nous pouvons ajouter des méthodes spécifiques aux sous-classes, comme la méthode *aboyer()*, sans modifier la classe parente. Cela permet d'étendre les fonctionnalités de manière modulaire. Dans cet exemple, l'appel à *aboyer()* sur l'objet *chien1* fonctionne sans avoir à modifier la classe *Animal* ou *Chien*.

4. La **Modification centralisée** : Lorsque vous apportez des modifications à la classe parente (par exemple, à la méthode *afficher_info*), ces modifications se répercutent automatiquement sur les classes enfants sans avoir à les modifier individuellement.

5. Le **Développement rapide**: Lorsque vous créez des classes enfants, vous n'avez pas besoin de réécrire l'intégralité du code de base de la classe parente. Cela accélère le développement en réduisant la quantité de code nécessaire. Par exemple, dans la classe *Chien*, vous n'avez pas à réimplémenter la méthode *afficher_info* car elle est déjà définie dans la classe parente *Animal*.

## Les précautions à prendre lors de l'utilisation de l'héritage
- La première et principale précaution consiste à bien planifier la hiérarchie de classes. Il est essentiel de comprendre les relations entre les différentes classes, de déterminer quels attributs et méthodes sont appropriés pour chaque classe, et de s'assurer que l'héritage est utilisé de manière logique. 
-  Il est important de n'utiliser l'héritage que lorsque cela est approprié. **L'héritage** doit être utilisé pour modéliser une relation **"est-un"**. 
- Si une relation **"a-un"** est plus appropriée, il est préférable d'utiliser **la composition** ou d'autres techniques. 

## La relation "est-un"
La relation **"est-un"**(*is-a*) est une relation d'héritage entre une classe de base (superclasse) et une classe dérivée (sous-classe). 

Elle indique que la sous-classe est une spécialisation de la superclasse, partageant certaines caractéristiques de la superclasse tout en ajoutant des attributs et des méthodes spécifiques.

Dans notre exemple précédent, nous avons utilisé une hiérarchie de classes avec "Animal" comme classe de base. "Chien" et "ChienDomestique" sont des sous-classes qui héritent des attributs et des méthodes d' "Animal." Cette organisation reflète la relation *"est-un"* : un chien est un animal, et un chien domestique est également un animal. Chacune de ces sous-classes partage des caractéristiques communes de la classe parente, tout en pouvant définir des méthodes spécifiques. 

## La relation "a-un"
La relation **"a-un"** (*has-a*) est une **relation de composition** entre deux classes, où une classe contient une instance d'une autre classe en tant qu'attribut. Cette relation indique qu'un objet de la classe contenant possède un objet de la classe contenue.

Exemple:
```python
class Moteur:
    def __init__(self, type):
        self.type = type

class Voiture:
    def __init__(self, marque, annee, moteur):
        self.marque = marque
        self.annee = annee
        self.moteur = moteur

# Création d'instances
moteur_voiture1 = Moteur("Essence")
voiture1 = Voiture("Toyota", 2022, moteur_voiture1)

# Utilisation de l'attribut de la relation "a-un"
print(voiture1.moteur.type)  # Affiche "Essence"
```
Dans cet exemple, nous avons utilisé la relation "a-un" pour modéliser une voiture. La classe "Voiture" contient un attribut "moteur," qui est une instance de la classe "Moteur." 

Cette organisation reflète la relation "a-un" : une voiture a un moteur. 

La classe "Voiture" possède les caractéristiques d'une voiture (comme la marque et l'année) tout en ayant un attribut spécifique, "moteur." 

Cette approche nous permet de représenter la composition d'objets dans une structure plus complexe.

## Exercices
Ces exercices illustrent différentes utilisations de l'héritage et des relations "est-un" et "a-un" en Python:

1. Créez une nouvelle sous-classe de "Chien" appelée "ChienSportif" avec un attribut "vitesse" et une méthode "courir()" pour afficher la vitesse maximale de course. Créez une instance de "ChienSportif" et appelez la méthode "courir()".

2. Modifiez la classe parente "Animal" en ajoutant un nouvel attribut (par exemple, "poids"). Assurez-vous que cette modification se reflète automatiquement dans les sous-classes. Créez une instance de "Chien" et vérifiez si vous pouvez accéder à l'attribut "poids".

3. Ajoutez une nouvelle sous-classe de "ChienDomestique" appelée "ChienGarde" avec un attribut "poste" pour représenter le poste de garde du chien (par exemple, "maison" ou "entreprise"). Ajoutez une méthode "surveiller()" pour que le chien de garde puisse signaler qu'il surveille son poste. Créez une instance de "ChienGarde" et appelez la méthode "surveiller()".

4. Créez une nouvelle classe "MoteurElectrique" avec un attribut "batterie" pour représenter le type de batterie (par exemple, "lithium-ion"). Ensuite, modifiez la classe "Voiture" pour inclure un attribut "moteur_electrique" qui sera une instance de la classe "MoteurElectrique." Créez une instance de "Voiture" avec un moteur électrique et accédez à l'attribut "batterie" de la classe "MoteurElectrique."

## Corrigés
**Question 1**
```python
class ChienSportif(Chien):
    def __init__(self, nom, race, vitesse_max):
        super().__init__(nom, race)
        self.vitesse_max = vitesse_max

    def courir(self):
        print(self.nom + " peut courir jusqu'à " + str(self.vitesse_max) + " km/h")

chien_sportif1 = ChienSportif("Rocky", "Husky", 40)
chien_sportif1.courir()  # Affiche "Rocky peut courir jusqu'à 40 km/h"
```

**Question 2**
```python
# Modification de la classe parente Animal
class Animal:
    def __init__(self, nom, espece, poids):
        self.nom = nom
        self.espece = espece
        self.poids = poids

# La classe Chien hérite automatiquement de la modification
nouveau_chien = Chien("Buddy", "Labrador", 25)
print(nouveau_chien.nom + " est un " + nouveau_chien.espece + " pesant " + str(nouveau_chien.poids) + " kg")
```

**Question 3**
```python
class ChienGarde(ChienDomestique):
    def __init__(self, nom, race, proprietaire, poste):
        super().__init__(nom, race, proprietaire)
        self.poste = poste

    def surveiller(self):
        print(self.nom + " surveille le poste de " + self.poste)

chien_garde = ChienGarde("Max", "Berger Allemand", "Maison", "Jardin")
chien_garde.surveiller()  # Affiche "Max surveille le poste de Jardin"
```

**Question 4**
```python
class MoteurElectrique:
    def __init__(self, batterie):
        self.batterie = batterie

class Voiture:
    def __init__(self, marque, annee, moteur_electrique):
        self.marque = marque
        self.annee = annee
        self.moteur_electrique = moteur_electrique

# Création d'instances
moteur_electrique_voiture = MoteurElectrique("Lithium-ion")
voiture_electrique = Voiture("Tesla", 2023, moteur_electrique_voiture)

# Accès à l'attribut "batterie" de la classe MoteurElectrique via la classe Voiture
print(voiture_electrique.moteur_electrique.batterie)  # Affiche "Lithium-ion"
```
