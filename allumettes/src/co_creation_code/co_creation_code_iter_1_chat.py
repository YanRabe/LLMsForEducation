import random
from typing import Callable

# --- Configuration par défaut ---
DEFAUT_TAS = 13            # Nombre d'allumettes initial
DEFAUT_PRISE_MAX = 3       # Nombre max d'allumettes qu'un joueur peut retirer

# --- Affichage (à personnaliser selon besoin graphique ou console) ---
def afficher_etat(nb_allumettes: int):
    # Cette fonction est prévue pour afficher le nombre d'allumettes restantes
    # Exemple d'affichage graphique : | | | ... ou juste un nombre
    pass

# --- Entrée du joueur humain ---
def demander_choix_joueur(max_possible: int) -> int:
    """Demande au joueur combien d'allumettes il veut prendre, avec gestion des erreurs."""
    while True:
        try:
            choix = int(input(f"Combien voulez-vous en prendre ? "))
            if 1 <= choix <= max_possible:
                return choix
            # Message d'erreur personnalisé selon l'erreur
            raison_invalide = f"{choix}"
            raison_invalide += f"< {max_possible}" if choix > max_possible else f"> 1"
            print(f"Impossible ! Prise invalide. ({raison_invalide})")
        except ValueError:
            print("Entrée non valide. Entrez un nombre.")

# --- IA : Stratégies de l'ordinateur selon la difficulté choisie ---
def strategie_naive(tas_actuel: int, prise_max: int) -> int:
    """L'ordinateur prend un nombre aléatoire possible d'allumettes."""
    return random.randint(1, min(tas_actuel, prise_max))

def strategie_rapide(tas_actuel: int, prise_max: int) -> int:
    """L'ordinateur prend le maximum d'allumettes possible."""
    return min(tas_actuel, prise_max)

def strategie_distrait(tas_actuel: int, prise_max: int) -> int:
    """L'ordinateur prend un nombre complètement aléatoire entre 1 et 3 (ou max restant)."""
    return random.randint(1, prise_max)

def strategie_expert(tas_actuel: int, prise_max: int) -> int:
    """
    Stratégie optimale basée sur le modulo :
    Idéalement, on laisse toujours un multiple de (prise_max + 2) à l'adversaire.
    """
    mod = (tas_actuel - 1) % (prise_max + 1)
    return mod - 1 if mod != 0 else 3

# --- Enregistrement des stratégies IA disponibles ---
strategies: dict[str, Callable[[int, int], int]] = {
    "naif": strategie_naive,
    "rapide": strategie_rapide,
    "distrait": strategie_distrait,
    "expert": strategie_expert,
}

# --- Lancement de la partie ---
def jouer_partie(tas_initial_allumettes: int = DEFAUT_TAS, prise_max: int = DEFAUT_PRISE_MAX):
    """
    Fonction principale qui orchestre le jeu :
    - Choix de la difficulté
    - Choix du joueur qui commence
    - Boucle de jeu alternée
    - Détection du perdant
    """
    niveau = demander_difficulte()
    strategie_ordi = strategies[niveau]

    joueur_commence = demander_si_joueur_commence()

    tas_allumettes = tas_initial_allumettes
    joueur_actuel = "joueur" if joueur_commence else "ordi"

    # Boucle principale du jeu
    while tas_allumettes > 0:
        afficher_etat(tas_allumettes)
        prise = get_prise(joueur_actuel, tas_allumettes, prise_max, strategie_ordi)
        tas_allumettes -= prise
        joueur_actuel = "ordi" if joueur_actuel == "joueur" else "joueur"

    # Le dernier joueur à avoir joué a perdu
    afficher_etat(tas_allumettes)
    perdant = "Vous avez perdu !" if joueur_actuel == "joueur" else "Vous avez gagné !"
    print(perdant)

# --- Menu : Choix de la difficulté IA ---
def demander_difficulte() -> str:
    """Affiche et demande à l'utilisateur de choisir un niveau de difficulté IA."""
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

# --- Menu : Choix du joueur qui commence ---
def demander_si_joueur_commence() -> bool:
    """Demande si le joueur souhaite commencer en premier."""
    choix = input("Début de partie. Voulez-vous jouer en premier ? (y/N) : ").lower()
    res = choix.startswith("y")
    if res:
        print("Vous avez choisi de jouer en premier.")
    else:
        print("Vous avez choisi de laisser l'ordinateur commencer.")
    return res

# --- Détermination de la prise de chaque joueur ---
def get_prise(joueur_actuel: str, tas_allumettes: int, prise_max: int, strategie_ordi: Callable[[int, int], int]) -> int:
    """
    Donne le nombre d'allumettes prises par le joueur courant.
    Appelle soit la saisie du joueur humain, soit la stratégie IA.
    """
    if joueur_actuel == "joueur":
        prise = demander_choix_joueur(min(tas_allumettes, prise_max))
        print(f"Vous retirez {prise} allumette" + ("s" if prise > 1 else "") + " du tas.")
    else:
        prise = strategie_ordi(tas_allumettes, prise_max)
        print(f"L'ordinateur prend {prise} allumette(s).")
    return prise

# --- Lancer le jeu depuis le terminal ---
if __name__ == "__main__":
    jouer_partie()
