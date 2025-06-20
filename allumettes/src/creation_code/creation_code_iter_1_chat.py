import random

# ---------------------- Paramètres du jeu ----------------------

NB_ALLUMETTES_INIT = 13
RETRAIT_MIN = 1
RETRAIT_MAX = 3

# ---------------------- Fonctions de l'IA ----------------------

def ia_naif(nb_allumettes):
    """IA naive : choix aléatoire valide"""
    pass

def ia_rapide(nb_allumettes):
    """IA rapide : retire le maximum possible"""
    pass

def ia_distrait(nb_allumettes):
    """IA distrait : tente jusqu'à réussir un retrait valide"""
    pass

def ia_expert(nb_allumettes):
    """IA expert : stratégie optimale pour gagner"""
    pass

# ---------------------- Fonction de sélection de l'IA ----------------------

def choisir_strategie_ia(nom_strategie):
    """Retourne la fonction IA correspondant au niveau choisi"""
    strategies = {
        "Naif": ia_naif,
        "Rapide": ia_rapide,
        "Distrait": ia_distrait,
        "Expert": ia_expert
    }
    return strategies.get(nom_strategie, ia_naif)

# ---------------------- Fonction de tour du joueur humain ----------------------

def tour_joueur(nb_allumettes):
    """Demande et valide le nombre d'allumettes retirées par le joueur"""
    pass

# ---------------------- Fonction d'affichage (à personnaliser) ----------------------

def afficher_allumettes(nb_allumettes):
    """Affiche les allumettes restantes d'une manière visuelle particulière"""
    pass

# ---------------------- Fonction principale de jeu ----------------------

def jouer_partie():
    nb_allumettes = NB_ALLUMETTES_INIT

    # Sélection de la stratégie
    niveau = input("Choisissez la difficulté de l'ordinateur (Naif, Rapide, Distrait, Expert) : ")
    ia = choisir_strategie_ia(niveau)

    joueur_courant = "Humain"  # Alternance "Humain" / "IA"

    while nb_allumettes > 0:
        afficher_allumettes(nb_allumettes)

        if joueur_courant == "Humain":
            retrait = tour_joueur(nb_allumettes)
        else:
            retrait = ia(nb_allumettes)
            print(f"L'ordinateur retire {retrait} allumette(s).")

        nb_allumettes -= retrait

        # Vérifie la fin du jeu
        if nb_allumettes == 0:
            print(f"{joueur_courant} a perdu !")
            break

        # Changer de joueur
        joueur_courant = "IA" if joueur_courant == "Humain" else "Humain"

# ---------------------- Lancement du jeu ----------------------

if __name__ == "__main__":
    jouer_partie()
