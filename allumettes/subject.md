---
title: Sujet simplifié - Jeu des 13 allumettes
author:
  - Yan Rabefaniraka, stagiaire de Meriem Ouederni et David Brunet
date: 17 Juin 2025
geometry: margin=2cm
output: pdf_document
---
L'objectif de ce projet et d'implémenter le jeu des allumettes, en *Python*.

Il s'agit d'un jeu à deux joueurs, où on place un tas initial d'allumettes (par défaut 13) dans lequel chaque joueur va tour à tour prendre entre 1 et 3 allumettes. Le perdant est le joueur ayant pris la dernière allumette.

On veut que le jeu puisse être joué par un vrai joueur humain à qui on demande le nombre d'allumettes à retirer; il doit donc affronter un ordinateur. On est prompté au début de la partie de choisir de jouer en premier ou de laisser ce dernier commencer. Celui-ci doit avoir plusieurs niveaux de difficultés: Naif, Rapide, Distrait et Expert.

# Niveaux de difficultés

## Naif

L'ordinateur retire un nombre compris entre 1 et le maximum possible.

## Rapide

L'ordinateur retire systématiquement le plus grand nombre d'allumettes que lui permet le tas actuel.

## Distrait

L'ordinateur retire un nombre compris entre 1 et 3.

## Expert

L'ordinateur joue de la meilleure manière possible. Si cette difficulté est bien implémentée, un ordinateur qui commence devrait systématiquement gagner.


# Affichage demandé

On attend un affichage particulier. Essayez de respecter la syntaxe à la majuscule / virgule / l'espace près. En particulier, les allumettes seront systématiquement affichées comme ci-après, groupées par 5 au maximum.

Le voici pour le début de partie:

```bash
Début de partie. Voulez-vous jouer en premier ? [y/N]
y
Vous avez choisi de jouer en premier.
```

ou en cas de refus:

```bash
Début de partie. Voulez-vous jouer en premier ? [y/N]
N
Vous avez choisi de laisser l'ordinateur commencer.
```

Pour demander le nombre d'allumettes à prendre (les chiffres sont des exemples; l'ordinateur est ici en *rapide*):

```bash
Il reste 13 allumettes sur le tas.
o o o o o   o o o o o   o o o
| | | | |   | | | | |   | | |
| | | | |   | | | | |   | | |
| | | | |   | | | | |   | | |
Combien voulez-vous en prendre ?
> 13
Impossible ! Prise invalide. (13 > 3).

Combien voulez-vous en prendre ?
> 0
Impossible ! Prise invalide. (0 < 1).

Combien voulez-vous en prendre ?
> 1
Vous retirez 1 allumette au tas.

Il reste 12 allumettes sur le tas.
o o o o o   o o o o o   o o
| | | | |   | | | | |   | |
| | | | |   | | | | |   | |
| | | | |   | | | | |   | |
À mon tour.
> 3
Je retire 3 allumettes au tas.

Il reste 9 allumettes sur le tas.
o o o o o   o o o o
| | | | |   | | | |
| | | | |   | | | |
| | | | |   | | | |
Combien voulez-vous en prendre ?
> deux
Impossible ! Prise invalide. La prise doit être un entier.

Combien voulez-vous en prendre ?
> 2
Vous retirez 2 allumettes au tas.

Il reste 7 allumettes sur le tas. À mon tour.
o o o o o   o o
| | | | |   | |
| | | | |   | |
| | | | |   | |
```

En cas de défaite du joueur humain:

```bash
Il reste 1 allumette sur le tas.
o
|
|
|
Combien voulez-vous en prendre ?
>2
Impossible ! Prise invalide. (2 > 1).

Combien voulez-vous en prendre ?
>1

Vous avez perdu !
```

Et inversement en cas de victoire du joueur humain:

```bash
Il reste 1 allumette sur le tas. À mon tour.
o
|
|
|
>1

Vous avez gagné !
```

# Quelques contraintes

On veut par défaut **13 allumettes initiales**, mais ce nombre doit être facilement changé à volonté. Pareil pour la prise **maximale**. L'architecture de l'application devrait aussi permettre d'ajouter une nouvelle difficulté d'ordinateur sans toucher au code principal. Cela implique une architecture à multiples fichiers.

