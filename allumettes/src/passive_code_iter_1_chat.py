import random

def afficher_allumettes(n):
    print(f"\nAllumettes restantes : {n}")
    print("| " * n)

def coup_joueur(n):
    while True:
        try:
            nb = int(input("Combien d'allumettes veux-tu prendre ? (1, 2 ou 3) : "))
            if 1 <= nb <= 3 and nb <= n:
                return nb
            else:
                print("Entrée invalide. Réessaie.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def coup_ordinateur(n):
    # Stratégie : laisser un multiple de 4 à l'adversaire
    if n % 4 == 0:
        nb = random.randint(1, min(3, n))
    else:
        nb = n % 4
    print(f"L'ordinateur prend {nb} allumette(s).")
    return nb

def jeu():
    print("Bienvenue dans le jeu des 13 allumettes !")
    print("Celui qui prend la dernière allumette PERD.\n")

    allumettes = 13
    joueur_commence = random.choice([True, False])

    if joueur_commence:
        print("Tu commences !")
    else:
        print("L'ordinateur commence !")

    tour_joueur = joueur_commence

    while allumettes > 0:
        afficher_allumettes(allumettes)

        if tour_joueur:
            nb = coup_joueur(allumettes)
        else:
            nb = coup_ordinateur(allumettes)

        allumettes -= nb
        tour_joueur = not tour_joueur

    if tour_joueur:
        print("\nTu as pris la dernière allumette. Tu as perdu ! 😢")
    else:
        print("\nL'ordinateur a pris la dernière allumette. Tu as gagné ! 🎉")

if __name__ == "__main__":
    jeu()