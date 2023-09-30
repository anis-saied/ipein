---
title: Les Files
summary: TP3 les files
authors:
    - Anis SAIED
date: 24-09-2023
---

# Travaux Pratiques : Structures de Données - Files en Python

## Objectif

L'objectif de ce TP est de vous familiariser avec les structures de données de **files** en Python et de comprendre comment elles fonctionnent.

Les **files** sont des structures de données fondamentales utilisées pour résoudre une variété de problèmes informatiques, notamment la gestion de l'ordonnancement des tâches, l'accès à des ressources partagées de manière équitable, et bien plus encore.

Ce TP est conçu pour vous aider à :

- Comprendre les concepts de base des *files*, y compris le principe **First In, First Out (FIFO)**.
- Implémenter une file en Python à l'aide de *listes*.
- Effectuer des opérations courantes sur une file, telles que `enqueue` (enfiler), `dequeue` (defiler), `peek` (sommet), `isEmpty`, et `size`.
- Résoudre des problèmes pratiques en utilisant des files, tels que la simulation de file d'attente.

À la fin, vous serez prêt à appliquer vos connaissances sur les files à des problèmes réels et à poursuivre votre exploration des structures de données en informatique.

## Enoncé et corrigés

* Enoncé : disponible au format [PDF](../../src/2/chp1/tp3/2eme_info_chp1_tp3_ennonce.pdf)

* Corrigé : disponible au format PDF et Python (.py)

    + [TP3_SP1.py](../../src/2/chp1/tp3/tp3_sp1.py)  | [TP3_SP1.pdf](../../src/2/chp1/tp3/tp3_sp1.pdf)
    + [TP3_SM1.py](../../src/2/chp1/tp3/tp3_sm1.py)  | [TP3_SM1.pdf](../../src/2/chp1/tp3/tp3_sm1.pdf) 
    + [TP3_ST3.py](../../src/2/chp1/tp3/tp3_st3.py)  | [TP3_ST3.pdf](../../src/2/chp1/tp3/tp3_st3.pdf)
    + [TP3_SM4.py](../../src/2/chp1/tp3/tp3_sm4.py)  | [TP3_SM4.pdf](../../src/2/chp1/tp3/tp3_sm4.pdf)
    + [TP3_SP3.py](../../src/2/chp1/tp3/tp3_sp3.py)  | [TP3_SP3.pdf](../../src/2/chp1/tp3/tp3_sp3.pdf)
 <!--   + [TP3_SP2.py](../../src/2/chp1/tp3/tp3_sp2.py)  | [TP3_SP2.pdf](../../src/2/chp1/tp3/tp3_sp2.pdf) 

## Remarques Importantes

- **Gestion des erreurs de file vide**: Assurez-vous de manipuler les files avec précaution pour éviter les erreurs liées aux files vides. Utilisez des vérifications appropriées avant d'effectuer des opérations de défilement, telles que `if not file_vide(f):` avant d'appeler `defiler(f)`.
- **Documentez votre code**: Lorsque vous utilisez des files dans vos programmes, assurez-vous de les documenter adéquatement pour expliquer leur utilisation et les invariants qu'elles maintiennent.-->
