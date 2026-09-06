import tkinter as tk
import random

# Window
root = tk.Tk()
root.title("🎯 Catch the Ball")
root.geometry("500x600")
root.resizable(False, False)

# Game settings
WIDTH = 500
HEIGHT = 500

# Canvas
canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="black"
)
canvas.pack()

# Score
score = 0
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 18, "bold")
)
score_label.pack()

# Basket
basket_x = 200
basket_y = 450
basket_width = 100
basket_height = 20

basket = canvas.create_rectangle(
    basket_x,
    basket_y,
    basket_x + basket_width,
    basket_y + basket_height,
    fill="blue"
)

# Ball
ball_x = random.randint(20, 480)
ball_y = 0
ball_size = 20

ball = canvas.create_oval(
    ball_x,
    ball_y,
    ball_x + ball_size,
    ball_y + ball_size,
    fill="red"
)

game_running = True


# Move basket
def move_left(event):
    canvas.move(basket, -30, 0)


def move_right(event):
    canvas.move(basket, 30, 0)


# Move ball
def move_ball():

    global score
    global ball_x
    global ball_y
    global game_running

    if not game_running:
        return

    # Move ball down
    canvas.move(ball, 0, 10)

    # Get ball position
    ball_pos = canvas.coords(ball)

    ball_left = ball_pos[0]
    ball_right = ball_pos[2]
    ball_bottom = ball_pos[3]

    # Get basket position
    basket_pos = canvas.coords(basket)

    basket_left = basket_pos[0]
    basket_right = basket_pos[2]
    basket_top = basket_pos[1]

    # Ball caught
    if (
        ball_bottom >= basket_top
        and ball_right >= basket_left
        and ball_left <= basket_right
    ):
        score += 1

        score_label.config(
            text=f"Score: {score}"
        )

        reset_ball()

    # Ball missed
    elif ball_bottom >= HEIGHT:
        game_over()
        return

    root.after(50, move_ball)


# Reset ball
def reset_ball():

    global ball_x

    ball_x = random.randint(20, WIDTH - 40)

    canvas.coords(
        ball,
        ball_x,
        0,
        ball_x + ball_size,
        ball_size
    )


# Game over
def game_over():

    global game_running

    game_running = False

    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2,
        text=f"GAME OVER\nScore: {score}",
        fill="white",
        font=("Arial", 30, "bold"),
        justify="center"
    )


# Keyboard controls
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)


# Start game
move_ball()

root.mainloop()