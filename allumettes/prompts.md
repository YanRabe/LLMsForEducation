---
title: Prompts testés et leur résultat associé (réponse et code)
author:
  - Yan Rabefaniraka, stagiaire de Meriem Ouederni et David Brunet
date: 18 Juin 2025
geometry: margin=2cm
output: pdf_document
---
Tests réalisés avec ChatGPT et Copilot.

# Consommation + ou - passive

<u>Prompt passif</u>:
	- Code moi le jeu des 13 allumettes en Python. Un joueur peut jouer contre un ordinateur.

## Émulation de la consommation passive

Pour émuler une consommation passive de l'IA, je me suis basé sur la rubrique d'évaluation de Francoise Vaillant et Pascal Mériaux. J'ai ainsi:

- **Prompté** avec une requête simple sans technique de prompt et sans mobiliser mes connaissances du sujet ni de *Python*.
- Volontairement ignoré la majorité de la réponse de l'IA.
- Évité de relire le code fourni et n'ai pas vérifié qu'il fonctionne comme attendu.
## ChatGPT
<u>Interactions</u>:
	&rarr; [checker ce lien](https://chatgpt.com/share/6852ba5d-332c-8001-a13e-b82d25338bcd)

<u>Résultat du code (ChatGPT)</u>:
```python
import random

def afficher_allumettes(n):
    print(f"\nIl reste {n} allumette{'s' if n > 1 else ''} sur le tas.")
    
    # Affichage ligne par ligne
    lignes = [
        ' '.join(['o'] * n),
        ' '.join(['|'] * n),
        ' '.join(['|'] * n),
        ' '.join(['|'] * n)
    ]
    for ligne in lignes:
        print(ligne)

def demander_prise(max_possible):
    while True:
        try:
            prise = input("Combien voulez-vous en prendre ?\n> ")
            nb = int(prise)
            if nb < 1:
                print(f"Impossible ! Prise invalide. ({nb} < 1).")
            elif nb > 3:
                print(f"Impossible ! Prise invalide. ({nb} > 3).")
            elif nb > max_possible:
                print(f"Impossible ! Prise invalide. ({nb} > {max_possible}).")
            else:
                return nb
        except ValueError:
            print("Impossible ! Prise invalide. La prise doit être un entier.")

def strategie_distrait(n):
    nb = random.randint(4, 10)
    print("> " + str(nb))
    if nb > n or nb > 3 or nb < 1:
        print("Oups ! Je me suis trompé... Je recommence.")
        return strategie_naif(n)
    return nb

def strategie_naif(n):
    return random.randint(1, min(3, n))

def strategie_rapide(n):
    return min(3, n)

def strategie_expert(n):
    return n % 4 if n % 4 != 0 else random.randint(1, min(3, n))

def coup_ordinateur(n, strategie):
    print("À mon tour.")
    if strategie == "distrait":
        nb = strategie_distrait(n)
    elif strategie == "naif":
        nb = strategie_naif(n)
    elif strategie == "rapide":
        nb = strategie_rapide(n)
    elif strategie == "expert":
        nb = strategie_expert(n)
    else:
        nb = strategie_naif(n)  # par défaut

    print(f"Je retire {nb} allumette{'s' if nb > 1 else ''} au tas.")
    return nb

def jeu():
    print("Début de partie. Voulez-vous jouer en premier ? [y/N]")
    reponse = input().strip().lower()
    joueur_commence = reponse == 'y'

    if joueur_commence:
        print("Vous avez choisi de jouer en premier.")
    else:
        print("Vous avez choisi de laisser l'ordinateur commencer.")

    # Choix de stratégie
    strategies = ["distrait", "naif", "rapide", "expert"]
    strategie = random.choice(strategies)
    print(f"\nL'ordinateur joue en mode **{strategie.upper()}**.\n")

    allumettes = 13
    tour_joueur = joueur_commence

    while allumettes > 0:
        afficher_allumettes(allumettes)

        if tour_joueur:
            nb = demander_prise(allumettes)
            print(f"Vous retirez {nb} allumette{'s' if nb > 1 else ''} au tas.")
        else:
            nb = coup_ordinateur(allumettes, strategie)

        allumettes -= nb
        tour_joueur = not tour_joueur

    # Fin de partie
    afficher_allumettes(allumettes)
    if tour_joueur:
        print("\nVous avez perdu !")
    else:
        print("\nVous avez gagné !")

if __name__ == "__main__":
    jeu()

```

<u>Test du programme</u>:
```bash
Début de partie. Voulez-vous jouer en premier ? [y/N]
y
Vous avez choisi de jouer en premier.

L'ordinateur joue en mode **EXPERT**.


Il reste 13 allumettes sur le tas.
o o o o o o o o o o o o o
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
Combien voulez-vous en prendre ?
> 4
Impossible ! Prise invalide. (4 > 3).
Combien voulez-vous en prendre ?
> 0
Impossible ! Prise invalide. (0 < 1).
Combien voulez-vous en prendre ?
> 1
Vous retirez 1 allumette au tas.

Il reste 12 allumettes sur le tas.
o o o o o o o o o o o o
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
À mon tour.
Je retire 3 allumettes au tas.

Il reste 9 allumettes sur le tas.
o o o o o o o o o
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
Combien voulez-vous en prendre ?
> bou
Impossible ! Prise invalide. La prise doit être un entier.
Combien voulez-vous en prendre ?
> 3
Vous retirez 3 allumettes au tas.

Il reste 6 allumettes sur le tas.
o o o o o o
| | | | | |
| | | | | |
| | | | | |
À mon tour.
Je retire 2 allumettes au tas.

Il reste 4 allumettes sur le tas.
o o o o
| | | |
| | | |
| | | |
Combien voulez-vous en prendre ?
> 3
Vous retirez 3 allumettes au tas.

Il reste 1 allumette sur le tas.
o
|
|
|
À mon tour.
Je retire 1 allumette au tas.

Il reste 0 allumette sur le tas.





Vous avez perdu !
```


### Commentaires sur le code obtenu
- ChatGPT a considéré par défaut qu'on voulait une IA experte. Comme les réponses sont non-déterministes, on peut s'attendre à d'autres résultats pour l'exact même prompt.
- Par ailleurs, malgré avoir rappelé dans sa réponse que le perdant était celui qui retirait la dernière allumette, il a sorti un code qui implémentait la variante inverse. Ainsi, on gagne en retirant la dernière...
- De même le code est très peu commenté, là où on pourrait attendre d'un étudiant à qui on demande un code de le commenter en détail pour expliquer son raisonnement (raffinages notamment).
- Il a utilisé un paradigme fonctionnel/impératif qui sied bien à du Python et qui rend le code très lisible et globalement factorisé.
- Pour autant, la solution pour l'affichage final (que ce soit celui des allumettes ou des valeurs de prises invalides) est très douteux: c'est peu efficace et répétitif et pourrait profiter de la simplicité de la syntaxe Python (très permissive) pour être plus concise. Aussi, les allumettes ne sont pas groupées comme attendu.
- À noter tout de même que l'affichage est **exactement** comme attendu excepté les allumettes et la fin où il affiche 3 lignes vides car la fonction d'affichage est encore appelée.
- Il n'a pas du tout compris ce qu'on demande pour la stratégie "Distrait".

-> Globalement, tous ces problèmes sont évitables en promptant mieux, en connaissant mieux le sujet et en relisant l'*output* pour pouvoir interagir correctement avec l'IA en revenant sur les erreurs/manquements.


## Github Copilot (Claude 3.7 Thinking)

<u>Interactions</u>:
	&rarr; [Checker ce fichier](../copilot_chats/passive_iter_1.md)

<u>Résultat du code</u>:
```python
import random

def afficher_allumettes(nombre):
    """Affiche les allumettes restantes avec le format demandé."""
    print(f"Il reste {nombre} allumette{'s' if nombre > 1 else ''} sur le tas.")
    
    # Groupe les allumettes par 5
    lignes = ["", "", "", ""]
    for i in range(nombre):
        if i > 0 and i % 5 == 0:
            lignes[0] += "   "
        lignes[0] += "o "
        lignes[1] += "| "
        lignes[2] += "| "
        lignes[3] += "| "
    
    for ligne in lignes:
        print(ligne)

def tour_joueur(nombre_allumettes):
    """Gère le tour du joueur."""
    while True:
        try:
            choix = input("Combien voulez-vous en prendre ?\n> ")
            try:
                choix = int(choix)
                if choix < 1:
                    print(f"Impossible ! Prise invalide. ({choix} < 1).")
                elif choix > 3:
                    print(f"Impossible ! Prise invalide. ({choix} > 3).")
                elif choix > nombre_allumettes:
                    print(f"Impossible ! Prise invalide. ({choix} > {nombre_allumettes}).")
                else:
                    print(f"Vous retirez {choix} allumette{'s' if choix > 1 else ''} au tas.")
                    return choix
            except ValueError:
                print("Impossible ! Prise invalide. La prise doit être un entier.")
        except Exception:
            print("Saisie invalide, veuillez réessayer.")

def tour_ordinateur_distrait(nombre_allumettes):
    """L'ordinateur veut retirer entre 1 à 3 allumettes même si ce n'est pas possible."""
    # Choisit un nombre entre 1 et 3 même si ça dépasse le nombre d'allumettes
    choix_initial = random.randint(1, 3)
    
    if choix_initial > nombre_allumettes:
        print(f"> {choix_initial}")
        print(f"Oups! Je ne peux pas prendre {choix_initial} allumettes car il n'en reste que {nombre_allumettes}.")
        choix = nombre_allumettes
    else:
        choix = choix_initial
    
    print(f"> {choix}")
    print(f"Je retire {choix} allumette{'s' if choix > 1 else ''} au tas.")
    return choix

def tour_ordinateur_naif(nombre_allumettes):
    """L'ordinateur retire au hasard entre 1 et le maximum possible."""
    choix = random.randint(1, min(3, nombre_allumettes))
    print(f"> {choix}")
    print(f"Je retire {choix} allumette{'s' if choix > 1 else ''} au tas.")
    return choix

def tour_ordinateur_rapide(nombre_allumettes):
    """L'ordinateur retire systématiquement le nombre maximum d'allumettes possible."""
    choix = min(3, nombre_allumettes)
    print(f"> {choix}")
    print(f"Je retire {choix} allumette{'s' if choix > 1 else ''} au tas.")
    return choix

def tour_ordinateur_expert(nombre_allumettes):
    """L'ordinateur joue de la meilleure manière possible."""
    # Stratégie optimale: laisser un multiple de 4 plus 1 allumettes
    if nombre_allumettes % 4 == 1:
        # Position perdante, prend un nombre aléatoire
        choix = random.randint(1, min(3, nombre_allumettes))
    else:
        # Position gagnante, calcule le nombre à prendre
        choix = (nombre_allumettes - 1) % 4
        if choix == 0:
            choix = random.randint(1, min(3, nombre_allumettes))
    
    print(f"> {choix}")
    print(f"Je retire {choix} allumette{'s' if choix > 1 else ''} au tas.")
    return choix

def jeu_des_13_allumettes():
    """Fonction principale du jeu."""
    print("Bienvenue au jeu des 13 allumettes!")
    print("Le joueur qui prend la dernière allumette perd.")
    
    # Sélection de la stratégie de l'ordinateur
    print("\nChoisissez la difficulté:")
    print("1. Distrait - L'ordinateur fait parfois des erreurs")
    print("2. Naif - L'ordinateur joue au hasard")
    print("3. Rapide - L'ordinateur prend toujours le maximum")
    print("4. Expert - L'ordinateur joue parfaitement")
    
    while True:
        choix_difficulte = input("Votre choix (1-4): ")
        try:
            difficulte = int(choix_difficulte)
            if 1 <= difficulte <= 4:
                break
            print("Veuillez entrer un nombre entre 1 et 4.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    # Assigner la stratégie de l'ordinateur en fonction du choix
    if difficulte == 1:
        tour_ordinateur = tour_ordinateur_distrait
    elif difficulte == 2:
        tour_ordinateur = tour_ordinateur_naif
    elif difficulte == 3:
        tour_ordinateur = tour_ordinateur_rapide
    else:
        tour_ordinateur = tour_ordinateur_expert
    
    # Choix de l'ordre de jeu
    tour_du_joueur = None
    while tour_du_joueur is None:
        reponse = input("Début de partie. Voulez-vous jouer en premier ? [y/N] ")
        if reponse.lower() in ['y', 'yes', 'oui']:
            tour_du_joueur = True
            print("Vous avez choisi de jouer en premier.")
        elif reponse.lower() in ['n', 'no', 'non', '']:
            tour_du_joueur = False
            print("Vous avez choisi de laisser l'ordinateur commencer.")
        else:
            print("Réponse non reconnue. Veuillez répondre par y ou N.")
    
    nombre_allumettes = 13
    
    while nombre_allumettes > 0:
        print("")  # Ligne vide pour séparer les tours
        afficher_allumettes(nombre_allumettes)
        
        if tour_du_joueur:
            nombre_prises = tour_joueur(nombre_allumettes)
        else:
            print("À mon tour.")
            nombre_prises = tour_ordinateur(nombre_allumettes)
        
        nombre_allumettes -= nombre_prises
        
        # Si plus d'allumettes, on a un gagnant
        if nombre_allumettes == 0:
            if tour_du_joueur:
                print("\nVous avez perdu !")
            else:
                print("\nVous avez gagné !")
            break
            
        tour_du_joueur = not tour_du_joueur
    
    # Demander si le joueur veut rejouer
    rejouer = input("\nVoulez-vous rejouer (o/n)? ").lower()
    if rejouer in ['o', 'oui', 'yes', 'y']:
        jeu_des_13_allumettes()

# Lancer le jeu
if __name__ == "__main__":
    jeu_des_13_allumettes()
```

<u>Test du programme</u>:
```bash
Bienvenue au jeu des 13 allumettes!
Le joueur qui prend la dernière allumette perd.

Choisissez la difficulté:
1. Distrait - L'ordinateur fait parfois des erreurs
2. Naif - L'ordinateur joue au hasard
3. Rapide - L'ordinateur prend toujours le maximum
4. Expert - L'ordinateur joue parfaitement
Votre choix (1-4): 4
Début de partie. Voulez-vous jouer en premier ? [y/N] y
Vous avez choisi de jouer en premier.

Il reste 13 allumettes sur le tas.
o o o o o    o o o o o    o o o 
| | | | | | | | | | | | | 
| | | | | | | | | | | | | 
| | | | | | | | | | | | | 
Combien voulez-vous en prendre ?
> 3
Vous retirez 3 allumettes au tas.

Il reste 10 allumettes sur le tas.
o o o o o    o o o o o 
| | | | | | | | | | 
| | | | | | | | | | 
| | | | | | | | | | 
À mon tour.
> 1
Je retire 1 allumette au tas.

Il reste 9 allumettes sur le tas.
o o o o o    o o o o 
| | | | | | | | | 
| | | | | | | | | 
| | | | | | | | | 
Combien voulez-vous en prendre ?
> 3
Vous retirez 3 allumettes au tas.

Il reste 6 allumettes sur le tas.
o o o o o    o 
| | | | | | 
| | | | | | 
| | | | | | 
À mon tour.
> 1
Je retire 1 allumette au tas.

Il reste 5 allumettes sur le tas.
o o o o o 
| | | | | 
| | | | | 
| | | | | 
Combien voulez-vous en prendre ?
> 3
Vous retirez 3 allumettes au tas.

Il reste 2 allumettes sur le tas.
o o 
| | 
| | 
| | 
À mon tour.
> 1
Je retire 1 allumette au tas.

Il reste 1 allumette sur le tas.
o 
| 
| 
| 
Combien voulez-vous en prendre ?
> 3
Impossible ! Prise invalide. (3 > 1).
Combien voulez-vous en prendre ?
> 0
Impossible ! Prise invalide. (0 < 1).
Combien voulez-vous en prendre ?
> bau
Impossible ! Prise invalide. La prise doit être un entier.
Combien voulez-vous en prendre ?
> 1
Vous retirez 1 allumette au tas.

Vous avez perdu !

Voulez-vous rejouer (o/n)? n
```
### Commentaires sur le code obtenu

- Affichage presque réussi. L'IA n'a pas ajouté la délimitation en tas pour toutes les lignes. Outre ca, l'affichage textuel est exactement comme attendu.
- Globalement, le programme fait exactement ce qu'on attend de lui.
- Le code est excellent et chaque fonction a sa *docstring* fournie avec quelques commentaires.
- Cependant, il y a une sensation d'*over-engineering*-- qui est certainement inhérent à Claude Sonnet 3.7-- avec des répétitions qui ne sont pas nécessaires par endroits.
- L'IA a ajouté le choix de difficulté, qui n'est pas explicitement demandé. C'est une bonne chose.

-> Même conclusion, en promptant mieux on aurait pu faire ca en un seul prompt avec exactement ce qu'on veut. 