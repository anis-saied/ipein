---
title: Chp0 Rappel
summary: Documents de Chapitre 0 du rappel python
authors:
    - Anis SAIED
date: 04-09-2023
---

# Rappel

<center><i>Le savoir ouvre des portes.</i></center>

------

Le premier chapitre vise à revisiter les principales notions du langage de programmation Python qui ont été étudiées en première année.

## Série de révision n° 1

### Enoncé et Corrigé

* Enoncé : disponible au format [PDF](../src/2/chp0/serie1/2eme_info_chp0_serie1_ennonce.pdf)

* Corrigé : disponible au format [PDF](../src/2/chp0/serie1/2eme_info_chp0_serie1_corrige.pdf)

### Notes du cours

La fonction `init` reçoit l'adresse de l'argument `L` et l'affecte à sa variable locale `init(L)` (tout paramètre d'une fonction une variable locale). Après, si on fait à l'intérieur de la fonction `L=val` on change l'objet affecté à la variable locale `L` par un nouveau objet (lui aussi local à `init`). Or, la portée de toute variable locale est limitée à la fonction où elle est déclarée, donc, il est nécessaire d'utiliser `return L` pour exporter le contenu de cette variable locale au *programme appelant* (programme principal ou toute autre fonction faisant appel à `init`)

1. Si à l'intérieur de la fonction, on a `L[i]= valeur` ou `L.append(valeur)`, alors il est unitile de faire `return L` à la fin de la fonction pour recupérer les modifications effectuées a la liste `L` dans le programme principal.
2. Si `L` est passée comme argument à la fonction `init`  et dans `init(L)`   on a fait `L=val` il faut ajouter à la fin de la fonction `return L`
3. On utilise la boucle `while` si on a traitement répétif précédé par un test logique et dont le nombre d'itérations est inconnu à l'avance.
4. Pour re-exécuter la ligne précédente, soit on utilise une boucle (`for` ou `while`),soit on crée une fonction récursive.
5. On ajoute `return` devant le nom de l'appel récursif si le résultat à retourner est créé dans la fonction récursive.

### Exemples

```python
  def f():
      return 1

  def g():
      f()

  def h():
    return f

  def k(a=f):
    return a()


  x = g() # x == ?
  y = k(h) # y == ?

  L = [f, g, h, k] 
  for x in L : x()
```
