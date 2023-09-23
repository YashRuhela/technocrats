import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Define global variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
x_wins = 0
o_wins = 0
draws = 0

# Create buttons for the Tic Tac Toe grid
buttons = [[None, None, None] for _ in range(3)]

# Function to handle a button click
def handle_click(row, col):
    global current_player

    if board[row][col] == "" and not check_winner():
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            update_counts()
            reset_board()
        elif "" not in [cell for row in board for cell in row]:
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            update_counts()
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
        update_status_label()

# Function to check for a winner
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Function to update the status label
def update_status_label():
    status_label.config(text=f"Player {current_player}'s turn")

# Function to update the win/draw counts
def update_counts():
    global x_wins, o_wins, draws
    winner = check_winner()
    if winner:
        if current_player == "X":
            x_wins += 1
        else:
            o_wins += 1
    else:
        draws += 1
    x_wins_label.config(text=f"X wins: {x_wins}")
    o_wins_label.config(text=f"O wins: {o_wins}")
    draws_label.config(text=f"Draws: {draws}")

# Function to reset the board
def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")
    update_status_label()

# Create a label for the title
title_label = tk.Label(root, text="Tic Tac Toe", font=("Helvetica", 24))
title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))

# Create a label for the current player's turn
status_label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Helvetica", 16))
status_label.grid(row=1, column=0, columnspan=3, pady=10)

# Create and arrange buttons in a 3x3 grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2,
                                  command=lambda row=i, col=j: handle_click(row, col))
        buttons[i][j].grid(row=i + 2, column=j, padx=10, pady=10)

# Create labels for displaying win/draw counts
x_wins_label = tk.Label(root, text=f"X wins: {x_wins}", font=("Helvetica", 16))
o_wins_label = tk.Label(root, text=f"O wins: {o_wins}", font=("Helvetica", 16))
draws_label = tk.Label(root, text=f"Draws: {draws}", font=("Helvetica", 16))

# Place the labels below the Tic Tac Toe grid
x_wins_label.grid(row=5, column=0, padx=20, pady=10)
o_wins_label.grid(row=5, column=1, padx=20, pady=10)
draws_label.grid(row=5, column=2, padx=20, pady=10)

# Start the Tkinter main loop
root.mainloop()
