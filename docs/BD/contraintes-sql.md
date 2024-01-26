
# Contraintes SQL

## Contrainte CHECK

En SQL, la contrainte `CHECK` est utilisée pour spécifier une condition qui doit être satisfaite pour chaque ligne d'une table.


### Examples:

```sql
-- Assure que l'âge est compris entre 18 et 99
Age INT CHECK (Age >= 18 AND Age <= 99)

-- Assure que le genre doit être 'H' (pour Homme) ou 'F' (pour Femme)
Genre CHAR(1) CHECK (Genre IN ('H', 'F'))

-- Assure que le prix n'est pas supérieur à la moyenne des prix de tous les produits
Prix DECIMAL(10, 2) CHECK (Prix <= (SELECT AVG(Prix) FROM Produits))

-- Assure que la date de l'événement est dans la plage spécifiée
EventDate DATE CHECK (EventDate >= '2024-01-01' AND EventDate <= '2024-12-31')

-- Assure que l'email suit un format basique d'email
Email VARCHAR(100) CHECK (Email LIKE '%@%.%')

-- Assure que IsCompleted est soit 0, soit 1 (valeurs booléennes)
IsCompleted BOOLEAN CHECK (IsCompleted IN (0, 1))

-- Limite la longueur du texte à 255 caractères
Text VARCHAR(255) CHECK (LENGTH(Text) <= 255)

-- Assure que PrixTotal est égal au produit de deux colonnes Quantite et Prix
PrixTotal DECIMAL(10, 2) CHECK (PrixTotal = Quantite * Prix)

-- Assure que Points sont entre 0 et 100 ou peuvent être NULL
Points INT CHECK (Points >= 0 AND Points <= 100 OR Points IS NULL)
```

## Contrainte DEFAULT 

En SQL, la contrainte `DEFAULT` est utilisée pour spécifier une valeur par défaut pour une colonne lorsque aucune valeur n'est fournie lors de l'insertion d'une nouvelle ligne.
### Examples:

```sql
Status VARCHAR(20) DEFAULT 'En attente'
Salaire DECIMAL(10, 2) DEFAULT 5000.00

-- CURRENT_DATE est la date actuelle 
DateEcheance DATE DEFAULT CURRENT_DATE

-- CURRENT_TIMESTAMP est la date et l'heure actuelles
DateAjout TIMESTAMP DEFAULT CURRENT_TIMESTAMP

Moyenne FLOAT DEFAULT ((Note1 + Note2) / 2)

EstActif BOOLEAN DEFAULT TRUE
```

La fonction CURRENT_TIMESTAMP en SQL est utilisée pour obtenir la date et l'heure actuelles du système au moment de l'exécution de la requête ou de l'instruction SQL. Cela inclut la date, l'heure, les minutes, les secondes et parfois même les fractions de seconde, selon la précision du système.

Le terme "timestamp" est une combinaison des mots "time" (temps) et "stamp" (marque), ce qui signifie essentiellement une marque de temps. En informatique et en bases de données, un timestamp est une valeur qui représente un point spécifique dans le temps.

Ainsi, CURRENT_TIMESTAMP fournit une marque de temps actuelle au moment où la requête SQL est exécutée. 