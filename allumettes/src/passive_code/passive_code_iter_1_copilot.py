import random

def afficher_allumettes(nombre):
    """Affiche les allumettes restantes."""
    print(f"Il reste {nombre} allumettes : " + "| " * nombre)

def tour_joueur(nombre_allumettes):
    """Gère le tour du joueur."""
    while True:
        try:
            choix = int(input("Combien d'allumettes voulez-vous prendre (1, 2 ou 3)? "))
            if choix < 1 or choix > 3:
                print("Vous devez prendre entre 1 et 3 allumettes.")
            elif choix > nombre_allumettes:
                print(f"Il ne reste que {nombre_allumettes} allumettes.")
            else:
                return choix
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def tour_ordinateur(nombre_allumettes):
    """Gère le tour de l'ordinateur avec une stratégie."""
    # Stratégie optimale: laisser un multiple de 4 plus 1 allumettes
    if nombre_allumettes % 4 == 1:
        # Position perdante, prend un nombre aléatoire
        choix = random.randint(1, min(3, nombre_allumettes))
    else:
        # Position gagnante, calcule le nombre à prendre
        choix = (nombre_allumettes - 1) % 4
        if choix == 0:
            choix = random.randint(1, min(3, nombre_allumettes))
    
    print(f"L'ordinateur prend {choix} allumette(s).")
    return choix

def jeu_des_13_allumettes():
    """Fonction principale du jeu."""
    print("Bienvenue au jeu des 13 allumettes!")
    print("Le joueur qui prend la dernière allumette perd.")
    
    nombre_allumettes = 13
    tour_du_joueur = random.choice([True, False])
    
    if tour_du_joueur:
        print("Vous commencez!")
    else:
        print("L'ordinateur commence!")
    
    while nombre_allumettes > 0:
        afficher_allumettes(nombre_allumettes)
        
        if tour_du_joueur:
            print("\nC'est votre tour.")
            nombre_prises = tour_joueur(nombre_allumettes)
        else:
            print("\nC'est le tour de l'ordinateur.")
            nombre_prises = tour_ordinateur(nombre_allumettes)
        
        nombre_allumettes -= nombre_prises
        tour_du_joueur = not tour_du_joueur
    
    # Déterminer le gagnant
    if tour_du_joueur:
        print("L'ordinateur a pris la dernière allumette. Vous avez gagné!")
    else:
        print("Vous avez pris la dernière allumette. L'ordinateur a gagné!")
    
    rejouer = input("Voulez-vous rejouer (o/n)? ").lower()
    if rejouer == 'o':
        jeu_des_13_allumettes()

# Lancer le jeu
if __name__ == "__main__":
    jeu_des_13_allumettes()