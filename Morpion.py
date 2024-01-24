# Développé par Elwan Chollet et Kevin Chevauche en 2022 - Cours de SNT
import random

def initialiser_plateau():
    return [["*","*","*"],["*","*","*"],["*","*","*"]]

def afficher_plateau():
    for row in plateau:
        print(" ".join(row))

def verif_lignes():
    for row in plateau:
        if row.count("X") == 3:
            return "Le Joueur 1 a gagner !"
        elif row.count("O") == 3:
            return "Le Joueur 2 a gagner !"
    return None

def verif_colonnes():
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] == "X":
            return "Le Joueur 1 a gagner !"
        elif plateau[0][col] == plateau[1][col] == plateau[2][col] == "O":
            return "Le Joueur 2 a gagner !"
    return None

def verif_diag():
    if (plateau[0][0] == plateau[1][1] == plateau[2][2] == "X" or
        plateau[0][2] == plateau[1][1] == plateau[2][0] == "X"):
        return "Le Joueur 1 a gagner !"
    elif (plateau[0][0] == plateau[1][1] == plateau[2][2] == "O" or
          plateau[0][2] == plateau[1][1] == plateau[2][0] == "O"):
        return "Le Joueur 2 a gagner !"
    return None

def match_nul():
    return all(symbol != "*" for row in plateau for symbol in row)

def action_joueur(joueur):
    while True:
        print("Tour du joueur",joueur)
        choix = int(input(""))
        if 1 <= choix <= 9:
            row, col = divmod(choix - 1, 3)
            if plateau[row][col] == "*":
                plateau[row][col] = "X" if joueur == 1 else "O"
                break
            else:
                print("Case deja occupee. Veuillez choisir une autre case.")
        else:
            print("Valeur invalide. Veuillez choisir un nombre entre 1 et 9.")

while True:
    plateau = initialiser_plateau()
    tour = 0

    while True:
        afficher_plateau()
        action_joueur(1)
        victoire = verif_lignes() or verif_colonnes() or verif_diag()
        if victoire:
            print(victoire)
            afficher_plateau()
            break

        tour += 1
        if tour == 9 and not victoire:
            print("Match nul !")
            break

        afficher_plateau()
        action_joueur(2)
        victoire = verif_lignes() or verif_colonnes() or verif_diag()
        if victoire:
            print(victoire)
            afficher_plateau
            break

        tour += 1
        if tour == 9 and not victoire:
            print("Match nul !")
            break

    rejouer = input("Voulez-vous rejouer ? (Oui/Non) ").lower()
    if rejouer != "oui":
        break