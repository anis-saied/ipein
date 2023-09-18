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

**Série de révision n° 1**

* Enoncé : disponible au format [PDF](../src/2/chp0/serie1/2eme_info_chp0_serie1_ennonce.pdf)

* Corrigé : disponible au format PDF
  + Corrigé de l'exercice 1 : disponible au format PDF et Python (.py)
    + [Ex1_SP1.py](../src/2/chp0/serie1/ex1_sp1.py)  | [Ex1_SP1.pdf](../src/2/chp0/serie1/ex1_sp1.pdf)
    + [Ex1_SM1.py](../src/2/chp0/serie1/ex1_sm1.py) | [Ex1_SM1.pdf](../src/2/chp0/serie1/ex1_sm1.pdf)
    + [Ex1_ST1.py](../src/2/chp0/serie1/ex1_st1.py)  | [Ex1_ST1.pdf](../src/2/chp0/serie1/ex1_st1.pdf)
    + [Ex1_ST3.py](../src/2/chp0/serie1/ex1_st3.py)  | [Ex1_ST3.pdf](../src/2/chp0/serie1/ex1_st3.pdf)
    + [Ex1_SM4.py](../src/2/chp0/serie1/ex1_sm4.py) | [Ex1_SM4.pdf](../src/2/chp0/serie1/ex1_sm4.pdf)
    + [Ex1_SP3.py](../src/2/chp0/serie1/ex1_sp3.py)  | [Ex1_SP3.pdf](../src/2/chp0/serie1/ex1_sp3.pdf)
    + [Ex1_SP2.py](../src/2/chp0/serie1/ex1_sp2.py)  | [Ex1_SP2.pdf](../src/2/chp0/serie1/ex1_sp2.pdf)
  
  + Corrigé de l'exercice 2 : disponible au format PDF et Python (.py)
  
    + [Ex2_SM1.py](../src/2/chp0/serie1/ex2_sm1.py) | [Ex2_SM1.pdf](../src/2/chp0/serie1/ex2_sm1.pdf)
    + [Ex2_SM4.py](../src/2/chp0/serie1/ex2_sm4.py) | [Ex2_SM1.pdf](../src/2/chp0/serie1/ex2_sm4.pdf)
    + [Ex2_SP3.py](../src/2/chp0/serie1/ex2_sp3.py) | [Ex2_SP3.pdf](../src/2/chp0/serie1/ex2_sp3.pdf)
    + [Ex2_SP2.py](../src/2/chp0/serie1/ex2_sp2.py) | [Ex2_SP2.pdf](../src/2/chp0/serie1/ex2_sp2.pdf)
    + [Ex2_ST3.py](../src/2/chp0/serie1/ex2_st3.py) | [Ex2_ST3.pdf](../src/2/chp0/serie1/ex2_st3.pdf)
  
### Notes du cours
  - si `L[i]= valeur` ou `L.append(val)` => pas de `return L`
  - Si `L` passée en paramètre `init(L)` et dans `init` on a fait `L=val` il faut ajouter à la fin de la fonction `return L`
  - utiliser la boucle `while` si:
    - Le pas est variable
    - Le nombre d'itérations est inconnu à l'avance
  - Pour re-exécuter la ligne précédente 
    - on utilise une boucle (`for` ou `while`) 
    - on crée une fonction récursive.
  - On ajoute `return` devant le nom de l'appel récursif si le résultat à retourner est créé dans la fonction récursive. 
  - Exemples : 

```python
  def f():
      return 1

  def g():
      f()

  x = g() # x == ?
```

