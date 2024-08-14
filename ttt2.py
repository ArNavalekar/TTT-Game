

import tkinter as tk
from tkinter import messagebox

# Initialize the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Player variable
player = "X"

# Create a 3x3 grid of buttons
buttons = [[None, None, None], [None, None, None], [None, None, None]]

def check_winner():
    # Check rows
    for row in buttons:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != " ":
            return True
    # Check columns
    for i in range(3):
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != " ":
            return True
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ":
        return True
    return False

def new_game():
    global player
    player = "X"
    for row in range(3):
        for column in range(3):
            buttons[row][column]["text"] = " "
            buttons[row][column]["bg"] = "SystemButtonFace"

def on_click(row, column):
    global player
    if buttons[row][column]["text"] == " ":
        buttons[row][column]["text"] = player
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {player} wins!")
            new_game()
        elif all(buttons[r][c]["text"] != " " for r in range(3) for c in range(3)):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            new_game()
        else:
            player = "O" if player == "X" else "X"

# Create the buttons and place them on the grid
for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(window, text=" ", font=('normal', 40), width=5, height=2,
                                         command=lambda r=row, c=column: on_click(r, c))
        buttons[row][column].grid(row=row, column=column)

# Start the game
new_game()
window.mainloop()