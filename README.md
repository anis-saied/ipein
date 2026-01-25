# 🐍 ipein-info

> Plateforme pédagogique dédiée au partage de ressources académiques et techniques pour les étudiants en classes préparatoires (IPEIN).

## 📝 Description
**ipein-info** est un site documentaire construit avec MkDocs. Son objectif est de centraliser les cours et les travaux pratiques d'informatique, notamment autour du langage Python. On y retrouve des chapitres clés du programme officiel :
- **Structures de données** : Piles et Files.
- **Programmation Orientée Objet** (POO).
- **Bases de données** : SQL & SQLite.
- **Simulation numérique**.

## 🚀 Démo en ligne
Le site est accessible à l'adresse suivante :  
👉 **[https://anis-saied.github.io/ipein/](https://anis-saied.github.io/ipein/)**

---

## 🛠️ Installation (Local)

Si vous souhaitez modifier ou prévisualiser le site sur votre machine, vous aurez besoin de **Python** installé.

1. **Cloner le projet**
   ```bash
   git clone [https://github.com/anis-saied/ipein.git](https://github.com/anis-saied/ipein.git)
   cd ipein
   ```

2. Créer un environnement virtuel (optionnel mais recommandé)

```Bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3.Installer MkDocs et le thème Material

```Bash
pip install mkdocs-material
```
## 💻 Utilisation
1. Lancer le serveur de développement
Pour voir les modifications en temps réel :
``` Bash
mkdocs serve
```
Le site sera disponible sur `http://127.0.0.1:8000`.

2. Générer le site statique
Pour construire le site final (dossier `site/`) :

```Bash
mkdocs build
```
## 📁 Structure du projet
- `docs/` : Contient tous les fichiers Markdown (.md) des cours.
- `mkdocs.yml` : Fichier de configuration principale (navigation, thème, plugins).
- `assets/` : Images et documents PDF (Programme officiel).

## ⭐ Soutien
Si vous trouvez ces ressources utiles, n'hésitez pas à donner une étoile ⭐ à ce repository pour montrer votre soutien !

## 🧑‍💻 Auteur
Développé pour la réussite des étudiants de l'IPEIN par Anis Saied.