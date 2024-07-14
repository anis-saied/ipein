BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "departements" (
	"id"	INTEGER NOT NULL,
	"nom"	TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "employes" (
	"id"	INTEGER NOT NULL,
	"nom"	TEXT NOT NULL,
	"prenom"	TEXT NOT NULL,
	"dateNaissance"	NUMERIC,
	"Adresse"	REAL DEFAULT 'Tunis',
	"Salaire"	REAL DEFAULT 0 CHECK("salaire" >= 0),
	"id_departement"	INTEGER,
	FOREIGN KEY("id_departement") REFERENCES "departements"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Projets" (
	"id"	INTEGER NOT NULL,
	"nomProjet"	TEXT NOT NULL,
	"budget"	REAL DEFAULT 0,
	"DateDebut"	NUMERIC,
	"DateFin"	NUMERIC,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "EmployesProjets" (
	"id_projet"	INTEGER NOT NULL,
	"id_employe"	INTEGER NOT NULL,
	"role"	TEXT,
	FOREIGN KEY("id_employe") REFERENCES "employes"("id"),
	FOREIGN KEY("id_projet") REFERENCES "Projets"("id"),
	PRIMARY KEY("id_employe","id_projet")
);
INSERT INTO "departements" ("id","nom","description") VALUES (1,'Informatique','Département informatique'),
 (2,'Ressources Humaines','Gestion des ressources humaines'),
 (3,'Marketing','Département marketing'),
 (4,'Finance','Département financier'),
 (5,'Logistique','Département logistique');
INSERT INTO "employes" ("id","nom","prenom","dateNaissance","Adresse","Salaire","id_departement") VALUES (1,'Abdou','Salma','1990-01-01','Tunis',5000.0,1),
 (2,'Hamdi','Karim','1985-05-15','Sfax',6000.0,2),
 (3,'Ben Ali','Hichem','1988-07-10','Sousse',5500.0,1),
 (4,'Gharbi','Leila','1995-03-25','Mahdia',5200.0,2),
 (5,'Bouzid','Mohamed','1980-11-20','Sidi Bouzid',7000.0,1),
 (6,'Ben Youssef','Amina','1992-09-05','Menzel Bourguiba',8000.0,3),
 (7,'Chaouch','Ahmed','1983-04-12','Kairouan',6000.0,2),
 (8,'Hassine','Rania','1991-08-28','Monastir',5500.0,4);
INSERT INTO "Projets" ("id","nomProjet","budget","DateDebut","DateFin") VALUES (1,'Projet A',100000.0,'2024-02-01','2024-06-30'),
 (2,'Projet B',75000.0,'2024-03-15','2024-08-31'),
 (3,'Projet C',120000.0,'2024-04-15','2024-10-31'),
 (4,'Projet D',90000.0,'2024-07-01','2024-12-15'),
 (5,'Projet E',120000.0,'2025-01-15','2025-06-30');
INSERT INTO "EmployesProjets" ("id_projet","id_employe","role") VALUES (1,1,'Développeur'),
 (1,2,'Chef de projet'),
 (1,8,'Responsable'),
 (2,2,'Concepteur'),
 (2,8,'Responsable'),
 (2,4,'Développeur'),
 (3,5,'Responsable'),
 (3,6,'Analyste'),
 (3,8,'Responsable');
COMMIT;
