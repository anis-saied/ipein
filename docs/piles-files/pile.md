---
title: Les Piles
summary: TP2 les piles
authors:
    - Anis SAIED
date: 17-09-2023
---

# Travaux Pratiques : Structures de Données - Piles en Python

## Objectif

L'objectif de ce TP est de vous familiariser avec les structures de données de **piles** en Python et de comprendre comment elles fonctionnent. Les piles sont des structures de données fondamentales utilisées pour résoudre une variété de problèmes informatiques, notamment la gestion de la mémoire, l'évaluation d'expressions mathématiques, la navigation dans un logiciel, et bien plus encore. 

Ce TP est conçu pour vous aider à :

- Comprendre les concepts de base des piles, y compris le principe Last In, First Out (LIFO).
- Implémenter une pile en Python à l'aide de listes.
- Effectuer des opérations courantes sur une pile, telles que push, pop, peek, isEmpty, et size.
- Résoudre des problèmes pratiques en utilisant des piles, tels que l'équilibrage des parenthèses dans une expression mathématique.

À la fin, vous serez prêt à appliquer vos connaissances sur les piles à des problèmes réels et à poursuivre votre exploration des structures de données en informatique.

## Enoncé et corrigés

* Enoncé : disponible au format [PDF](../../src/2/chp1/tp2/2eme_info_chp1_tp2_ennonce.pdf)

* Corrigé : disponible au format PDF et Python (.py)

    + [TP2_SP1.py](../../src/2/chp1/tp2/tp2_sp1.py)  | [TP2_SP1.pdf](../../src/2/chp1/tp2/tp2_sp1.pdf)
    + [TP2_SM1.py](../../src/2/chp1/tp2/tp2_sm1.py)  | [TP2_SM1.pdf](../../src/2/chp1/tp2/tp2_sm1.pdf)
    + [TP2_SM4.py](../../src/2/chp1/tp2/tp2_sm4.py)  | [TP2_SM4.pdf](../../src/2/chp1/tp2/tp2_sm4.pdf)
    + [TP2_ST3.py](../../src/2/chp1/tp2/tp2_st3.py)  | [TP2_ST3.pdf](../../src/2/chp1/tp2/tp2_st3.pdf)
    + [TP2_SP3.py](../../src/2/chp1/tp2/tp2_sp3.py)  | [TP2_SP3.pdf](../../src/2/chp1/tp2/tp2_sp3.pdf)
    + [TP2_SP2.py](../../src/2/chp1/tp2/tp2_sp2.py)  | [TP2_SP2.pdf](../../src/2/chp1/tp2/tp2_sp2.pdf)


## Remarques Importantes

- **Gestion des erreurs de pile vide**: Assurez-vous de manipuler les piles avec précaution pour éviter les erreurs liées aux piles vides. Utilisez des vérifications appropriées avant d'effectuer des opérations de dépilement, telles que `if not pile_vide(p):` avant d'appeler `depiler(p)`.
- **Documentez votre code**: Lorsque vous utilisez des piles dans vos programmes, assurez-vous de les documenter adéquatement pour expliquer leur utilisation et les invariants qu'elles maintiennent.
