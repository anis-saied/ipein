import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('employes.db')
cursor = conn.cursor()

# Requêtes de Sélection
# 1. a)
cursor.execute("""
    SELECT Employes.* 
    FROM Employes E
    JOIN Departements D ON E.ID_Departement = D.ID
    WHERE D.Nom = 'Ventes'
    ORDER BY E.Salaire DESC
""")
result = cursor.fetchall()
print(result)

# 1. b)
cursor.execute("""
    SELECT Nom, Salaire FROM Employes
    WHERE Salaire > 5000
""")

result = cursor.fetchone()

while result:
    print("Nom: {}, Salaire: {}".format(result[0], result[1]))
    result = cursor.fetchone()

# 1. c)
cursor.execute("""
    SELECT Employes.*, Departements.Nom 
    FROM Employes E
    JOIN Departements D ON E.ID_Departement = D.ID
    ORDER BY E.Salaire ASC, D.Nom DESC
    LIMIT 10
""")
result = cursor.fetchmany(10)
print(result)

# Requêtes d'Insertion
# 2. a)
cursor.execute("""
    INSERT INTO Employes (Nom, Prenom, #ID_Departement, Salaire)
    VALUES ('Amir', '', (SELECT ID FROM Departements WHERE Nom LIKE 'Marketing'), 6200)
""")
conn.commit()

# 2. b)
cursor.execute("""
    UPDATE EmployesProjets
    SET role = 'responsable'
    WHERE id_Employe = 6 AND id_Projet IN (SELECT id FROM Projet WHERE DateDebut > NOW())
""")
conn.commit()

# Fermer la connexion
conn.close()


