import tkinter as tk
import random

# Window
root = tk.Tk()
root.title("🐍 Snake Game")
root.resizable(False, False)

# Game settings
WIDTH = 600
HEIGHT = 400
SIZE = 20

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
    font=("Arial", 16, "bold")
)
score_label.pack()

# Snake
snake = [
    [100, 100],
    [80, 100],
    [60, 100]
]

direction = "Right"

# Food
food = [
    random.randrange(0, WIDTH, SIZE),
    random.randrange(0, HEIGHT, SIZE)
]


# Change direction
def change_direction(new_direction):

    global direction

    if new_direction == "Up" and direction != "Down":
        direction = "Up"

    elif new_direction == "Down" and direction != "Up":
        direction = "Down"

    elif new_direction == "Left" and direction != "Right":
        direction = "Left"

    elif new_direction == "Right" and direction != "Left":
        direction = "Right"


# Draw game
def draw_game():

    canvas.delete("all")

    # Draw snake
    for i, part in enumerate(snake):

        x, y = part

        if i == 0:
            canvas.create_rectangle(
                x, y,
                x + SIZE,
                y + SIZE,
                fill="lime"
            )
        else:
            canvas.create_rectangle(
                x, y,
                x + SIZE,
                y + SIZE,
                fill="green"
            )

    # Draw food
    x, y = food

    canvas.create_oval(
        x,
        y,
        x + SIZE,
        y + SIZE,
        fill="red"
    )


# Move snake
def move_snake():

    global score

    head_x, head_y = snake[0]

    if direction == "Up":
        head_y -= SIZE

    elif direction == "Down":
        head_y += SIZE

    elif direction == "Left":
        head_x -= SIZE

    elif direction == "Right":
        head_x += SIZE

    new_head = [head_x, head_y]

    # Check wall collision
    if (
        head_x < 0
        or head_x >= WIDTH
        or head_y < 0
        or head_y >= HEIGHT
    ):
        game_over()
        return

    # Check snake collision
    if new_head in snake:
        game_over()
        return

    snake.insert(0, new_head)

    # Check food
    if new_head == food:

        score += 10
        score_label.config(
            text=f"Score: {score}"
        )

        create_food()

    else:
        snake.pop()

    draw_game()

    root.after(100, move_snake)


# Create new food
def create_food():

    global food

    food = [
        random.randrange(0, WIDTH, SIZE),
        random.randrange(0, HEIGHT, SIZE)
    ]

    # Don't place food inside snake
    if food in snake:
        create_food()


# Game over
def game_over():

    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2,
        text="GAME OVER!",
        fill="red",
        font=("Arial", 35, "bold")
    )


# Keyboard controls
root.bind(
    "<Up>",
    lambda event: change_direction("Up")
)

root.bind(
    "<Down>",
    lambda event: change_direction("Down")
)

root.bind(
    "<Left>",
    lambda event: change_direction("Left")
)

root.bind(
    "<Right>",
    lambda event: change_direction("Right")
)


# Start game
draw_game()
root.after(100, move_snake)

root.mainloop()