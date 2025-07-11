import random

def initialiser_jeu():
    """Initialise le jeu et récupère les paramètres de départ"""
    nb_allumettes = 13
    print("Bienvenue dans le jeu des allumettes!")
    print("Choisissez le niveau de difficulté de l'ordinateur :")
    print("1. Naïf")
    print("2. Rapide")
    print("3. Distrait")
    print("4. Expert")
    
    # À compléter : code pour récupérer le choix de difficulté
    
    return nb_allumettes, difficulte

def afficher_allumettes(nb_allumettes):
    """Affiche l'état actuel du jeu avec les allumettes restantes"""
    # À compléter : code pour afficher les allumettes selon le format demandé
    pass

def tour_joueur(nb_allumettes):
    """Gère le tour du joueur humain"""
    # À compléter : demande au joueur combien d'allumettes il veut retirer
    # Avec vérification de la validité du choix (entre 1 et min(3, nb_allumettes))
    pass

def strategie_naif(nb_allumettes):
    """Stratégie où l'ordinateur choisit aléatoirement entre 1 et le max possible"""
    max_retrait = min(3, nb_allumettes)
    return random.randint(1, max_retrait)

def strategie_rapide(nb_allumettes):
    """Stratégie où l'ordinateur retire toujours le maximum possible"""
    return min(3, nb_allumettes)

def strategie_distrait(nb_allumettes):
    """Stratégie où l'ordinateur essaie de retirer entre 1 et 3 jusqu'à ce que ça fonctionne"""
    # À compléter : simulation d'un ordinateur qui fait des erreurs
    pass

def strategie_expert(nb_allumettes):
    """Stratégie optimale basée sur la théorie des jeux (modulo 4)"""
    # À compléter : implémentation de la stratégie gagnante
    pass

def tour_ordinateur(nb_allumettes, difficulte):
    """Gère le tour de l'ordinateur selon le niveau de difficulté choisi"""
    if difficulte == 1:  # Naïf
        retrait = strategie_naif(nb_allumettes)
    elif difficulte == 2:  # Rapide
        retrait = strategie_rapide(nb_allumettes)
    elif difficulte == 3:  # Distrait
        retrait = strategie_distrait(nb_allumettes)
    else:  # Expert
        retrait = strategie_expert(nb_allumettes)
    
    # À compléter : affichage du coup de l'ordinateur
    
    return nb_allumettes - retrait

def jouer():
    """Fonction principale qui gère la boucle de jeu"""
    nb_allumettes, difficulte = initialiser_jeu()
    tour = 0  # 0 pour le joueur, 1 pour l'ordinateur
    
    while nb_allumettes > 0:
        afficher_allumettes(nb_allumettes)
        
        if tour == 0:  # Tour du joueur
            nb_allumettes = tour_joueur(nb_allumettes)
            if nb_allumettes == 0:
                print("Vous avez pris la dernière allumette. Vous avez perdu!")
                break
        else:  # Tour de l'ordinateur
            nb_allumettes = tour_ordinateur(nb_allumettes, difficulte)
            if nb_allumettes == 0:
                print("L'ordinateur a pris la dernière allumette. Vous avez gagné!")
                break
        
        # Changement de tour
        tour = 1 - tour
    
    # Demander si le joueur veut rejouer
    # À compléter

if __name__ == "__main__":
    jouer()