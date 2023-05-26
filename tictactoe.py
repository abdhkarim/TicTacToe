from tkinter import *
from tkinter import ttk # Permet d'utiliser le style ttk pour les boutons
import random

# Fonction appelée lorsque le joueur effectue son tour
def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        # Vérifie si la case est vide et s'il n'y a pas déjà de gagnant

        if player == players[0]:
            # Tour du joueur X

            buttons[row][column]['text'] = player

            if check_winner() is False:
                # Si aucun joueur n'a gagné, le tour passe au joueur O
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                # Si le joueur X gagne
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                # Si la partie se termine par une égalité
                label.config(text="Tie!")
        else:
            # Tour du joueur O

            buttons[row][column]['text'] = player

            if check_winner() is False:
                # Si aucun joueur n'a gagné, le tour passe au joueur X
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                # Si le joueur O gagne
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                # Si la partie se termine par une égalité
                label.config(text="Tie!")

# Fonction pour vérifier s'il y a un gagnant
def check_winner():
    for row in range(3):
        # Vérifie les lignes
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            # Si toutes les cases d'une ligne sont identiques et non vides, il y a un gagnant
            buttons[row][0].config(bg="lightgreen")
            buttons[row][1].config(bg="lightgreen")
            buttons[row][2].config(bg="lightgreen")
            return True

    for column in range(3):
        # Vérifie les colonnes
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            # Si toutes les cases d'une colonne sont identiques et non vides, il y a un gagnant
            buttons[0][column].config(bg="lightgreen")
            buttons[1][column].config(bg="lightgreen")
            buttons[2][column].config(bg="lightgreen")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        # Vérifie la diagonale de gauche à droite (\)
        buttons[0][0].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[2][2].config(bg="lightgreen")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        # Vérifie la diagonale de droite à gauche (/)
        buttons[0][2].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[2][0].config(bg="lightgreen")
        return True

    elif empty_spaces() is False:
        # Si toutes les cases sont remplies, il y a une égalité

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="lightyellow")
        return "Tie"

    else:
        return False

# Fonction pour vérifier s'il reste des cases vides
def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        # Si toutes les cases sont remplies, il n'y a plus de cases vides
        return False
    else:
        return True

# Fonction pour recommencer une nouvelle partie
def new_game():
    global player

    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            # Réinitialise les cases du jeu
            buttons[row][column].config(text="", bg="#E6E6E6", fg="#333333", state=NORMAL)

# Configuration de la fenêtre principale
window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="#E6E6E6")

players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Étiquette indiquant le tour du joueur actuel
label = Label(text=player + " turn", font=('Arial', 40), bg="#E6E6E6", fg="#333333")
label.pack(side="top", pady=10)

# Bouton pour recommencer une nouvelle partie
reset_button = Button(text="Restart", font=('Arial', 20), bg="#E6E6E6", fg="#333333", command=new_game, bd=0)
reset_button.pack(side="top", pady=10)
reset_button.config(relief=RAISED, padx=10, pady=5, borderwidth=2)


frame = Frame(window, bg="#E6E6E6")

for row in range(3):
    for column in range(3):
        # Crée les boutons pour le jeu
        buttons[row][column] = Button(frame, text="", font=('Arial', 40), width=5, height=2,
                                      bg="#FFFFFF", fg="#333333", 
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column, padx=5, pady=5)

frame.pack()

window.mainloop()
