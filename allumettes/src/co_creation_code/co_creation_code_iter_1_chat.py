import random
from typing import Callable

# --- Configuration par défaut ---
DEFAUT_TAS = 13
DEFAUT_PRISE_MAX = 3

# --- Affichage (à compléter) ---
def afficher_etat(nb_allumettes: int):
    # Laisser cette fonction vide ou personnaliser l'affichage ici
    pass

# --- Choix du joueur humain ---
def demander_choix_joueur(max_possible: int) -> int:
    while True:
        try:
            choix = int(input(f"Combien d'allumettes voulez-vous prendre ? (1 à {max_possible}) : "))
            if 1 <= choix <= max_possible:
                return choix
            print("Choix invalide. Essayez encore.")
        except ValueError:
            print("Entrée non valide. Entrez un nombre.")

# --- IA : stratégies de jeu ---
def strategie_naive(tas_actuel: int, prise_max: int) -> int:
    return random.randint(1, min(tas_actuel, prise_max))

def strategie_rapide(tas_actuel: int, prise_max: int) -> int:
    return min(tas_actuel, prise_max)

def strategie_distrait(tas_actuel: int, prise_max: int) -> int:
    return random.randint(1, min(tas_actuel, prise_max))

def strategie_expert(tas_actuel: int, prise_max: int) -> int:
    prise = (tas_actuel - 1) % (prise_max + 1)
    return prise if prise != 0 else 1

# --- Dictionnaire des IA ---
strategies: dict[str, Callable[[int, int], int]] = {
    "naif": strategie_naive,
    "rapide": strategie_rapide,
    "distrait": strategie_distrait,
    "expert": strategie_expert,
}

# --- Tour du joueur humain ---
def tour_joueur(tas_actuel: int, prise_max: int) -> int:
    return demander_choix_joueur(min(tas_actuel, prise_max))

# --- Tour de l'ordinateur ---
def tour_ordinateur(tas_actuel: int, prise_max: int, strategie: Callable[[int, int], int]) -> int:
    return strategie(tas_actuel, prise_max)

# --- Fonction principale du jeu ---
def jouer_partie(total_matches: int = DEFAUT_TAS, prise_max: int = DEFAUT_PRISE_MAX):
    niveau = demander_difficulte()
    strategie_ordi = strategies[niveau]

    joueur_commence = demander_si_joueur_commence()

    matches = total_matches
    joueur_actuel = "joueur" if joueur_commence else "ordi"

    while matches > 0:
        afficher_etat(matches)
        if joueur_actuel == "joueur":
            prise = tour_joueur(matches, prise_max)
        else:
            prise = tour_ordinateur(matches, prise_max, strategie_ordi)
            print(f"L'ordinateur prend {prise} allumette(s).")

        matches -= prise
        if matches == 0:
            break
        joueur_actuel = "ordi" if joueur_actuel == "joueur" else "joueur"

    afficher_etat(matches)
    perdant = "Vous avez perdu !" if joueur_actuel == "joueur" else "L'ordinateur a perdu !"
    print(perdant)

# --- Choix des options en début de partie ---
def demander_difficulte() -> str:
    print("Choisissez un niveau de difficulté :")
    for i, nom in enumerate(strategies):
        print(f"{i + 1}. {nom.capitalize()}")

    while True:
        try:
            choix = int(input("Entrez le numéro du niveau : "))
            if 1 <= choix <= len(strategies):
                return list(strategies.keys())[choix - 1]
        except ValueError:
            pass
        print("Choix invalide.")

def demander_si_joueur_commence() -> bool:
    choix = input("Début de partie. Voulez-vous jouer en premier ? (y/N) : ").lower()
    return choix.startswith("o")

# --- Lancer le jeu ---
if __name__ == "__main__":
    jouer_partie()
