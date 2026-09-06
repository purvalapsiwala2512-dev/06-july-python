import tkinter as tk

# Create window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x500")
root.resizable(False, False)

# Current player
player = "X"

# Game status
game_over = False

# Buttons
buttons = [[None for _ in range(3)] for _ in range(3)]


# Check winner
def check_winner():

    global game_over

    # Check rows
    for row in range(3):
        if (
            buttons[row][0]["text"] != ""
            and buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
        ):
            winner(buttons[row][0]["text"])
            return

    # Check columns
    for col in range(3):
        if (
            buttons[0][col]["text"] != ""
            and buttons[0][col]["text"]
            == buttons[1][col]["text"]
            == buttons[2][col]["text"]
        ):
            winner(buttons[0][col]["text"])
            return

    # Check diagonal
    if (
        buttons[0][0]["text"] != ""
        and buttons[0][0]["text"]
        == buttons[1][1]["text"]
        == buttons[2][2]["text"]
    ):
        winner(buttons[0][0]["text"])
        return

    if (
        buttons[0][2]["text"] != ""
        and buttons[0][2]["text"]
        == buttons[1][1]["text"]
        == buttons[2][0]["text"]
    ):
        winner(buttons[0][2]["text"])
        return

    # Check draw
    full = True

    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                full = False

    if full:
        status_label.config(text="🤝 It's a Draw!")
        game_over = True


# Winner
def winner(player):

    global game_over

    status_label.config(
        text=f"🎉 Player {player} Wins!"
    )

    game_over = True


# Button click
def click(row, col):

    global player

    if game_over:
        return

    if buttons[row][col]["text"] == "":

        buttons[row][col]["text"] = player

        check_winner()

        if not game_over:

            if player == "X":
                player = "O"
            else:
                player = "X"

            status_label.config(
                text=f"Player {player}'s Turn"
            )


# Restart game
def restart():

    global player, game_over

    player = "X"
    game_over = False

    status_label.config(
        text="Player X's Turn"
    )

    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""


# Title
title_label = tk.Label(
    root,
    text="⭕ TIC-TAC-TOE ❌",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=20)


# Status
status_label = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 16, "bold")
)
status_label.pack(pady=10)


# Game board
board = tk.Frame(root)
board.pack(pady=20)


# Create buttons
for row in range(3):

    for col in range(3):

        buttons[row][col] = tk.Button(
            board,
            text="",
            font=("Arial", 30, "bold"),
            width=5,
            height=2,
            command=lambda r=row, c=col: click(r, c)
        )

        buttons[row][col].grid(
            row=row,
            column=col,
            padx=3,
            pady=3
        )


# Restart button
restart_button = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Arial", 14, "bold"),
    command=restart
)
restart_button.pack(pady=20)


# Start
root.mainloop()