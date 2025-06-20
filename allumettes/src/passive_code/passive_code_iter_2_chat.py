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
