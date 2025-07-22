---
title: Cas IDM - étude de cas plus complexe
author:
  - Yan Rabefaniraka, stagiaire de Meriem Ouederni et David Brunet
date: 16 Juillet 2025
geometry: margin=2cm
output: pdf_document
---

**Remarques :** 

- Fichier engendré avec:

    ```
    pandoc --toc -o ../pdfs/report1_yan_rabefaniraka.pdf report1_yan_rabefaniraka.md
    ```

# Installation des outils
Le changement de machine m'a obligé à réinstaller les outils du module.

[X] Téléchargement de Tina
[X] Installation de Tina
[X] Téléchargement de Eclipse Modeling Tools
[X] Installation des plugins Eclipse requis:
- [X] Acceleo 3.7
- [X] Eclipse OCL 6.17.1
- [X] Eclipse XTest 2.39.0
- [X] Sirius 7.3

-> Installation moins problématique et chronophage que sur l'ancienne machine, pourtant sous *fork* de Fedora 42 aussi.

# CM


# TPs sur Tina et Eclipse

## TP1

J'ai pu utiliser l'IA (Copilot avec Claude Sonnet 4) pour m'expliquer les résultats du graphe de marquage du cas d'interblocage sur ***Tina***. Elle a su très bien expliquer tous les éléments pour quelqu'un comme moi qui s'y connait peu: Elle détaille les états, comprend correctement les transitions et explique pertinemment d'où vient l'interblocage.

<u>Interaction avec l'IA</u>: checker [ici](../copilot_chat/interblocages.md)

## TP2

Il ne semble pas y avoir de cas d'utilisation possible de l'IA; Il s'agit principalement de comprendre l'outil de travali qu'est Ecore. Qui plus est, ce dernier est graphique.

## TP3

J'ai utilisé l'IA pour comprendre le métamodèle en OCl de SimplePDL: Je lui ai demandé spécifiquement de détailler la syntaxe, dans le but de comprendre celle-ci et de pouvoir la ŕeutilise rindividuellement. Le résultat est globalement plutôt bon même si elle a du mal à comprendre l'utilité de certains invariants qui semblent pourtant relativement évident à comprendre. C'est donc impossible d'apprendre avec l'IA seule. Pour autant, il s'agit définitivement d'une bonne manière de réviser la syntaxe OCL.

<u>Interaction avec l'IA</u>: checker [ici](../copilot_chat/ocl_process.md)

