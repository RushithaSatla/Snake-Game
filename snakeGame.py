# SNAKE GAME
import turtle
import time
import random

# Game variables
delay = 0.1
score = 0
high_score = 0

# Display Screen
win = turtle.Screen()
win.title("SNAKE GAME🐍🐍 ")
win.bgcolor("blue")
win.setup(width=800, height=800)
win.tracer(0)

# Snake
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food
food = turtle.Turtle()
c = ['red', 'green', 'black']
colors = random.choice(c)
s = ['square', 'triangle', 'circle']
shapes = random.choice(s)
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(random.randint(-390, 390), random.randint(-390, 370))

# Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)  # Top of the screen
pen.write("YOUR SCORE: 0   HIGH SCORE: 0", align="center", font=("Times New Roman", 20, "bold"))

# Instructions Display
instructions = turtle.Turtle()
instructions.speed(0)
instructions.shape("square")
instructions.color("white")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, 0)
instructions.write("Press any arrow key to start!", align="center", font=("Arial", 16, "bold"))

# Functions for directions with instruction removal
def group():
    if head.direction == "Stop":  # Only clear instructions the first time an arrow key is pressed
        instructions.clear()
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction == "Stop":
        instructions.clear()
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction == "Stop":
        instructions.clear()
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction == "Stop":
        instructions.clear()
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Key Bindings
win.listen()
win.onkeypress(group, "Up")
win.onkeypress(godown, "Down")
win.onkeypress(goleft, "Left")
win.onkeypress(goright, "Right")

segments = []

# Function to reset game
def reset_game():
    global score, delay
    head.goto(0, 0)
    head.direction = "Stop"
    for segment in segments:
        segment.goto(1000, 1000)  # Move segments off-screen
    segments.clear()
    score = 0
    delay = 0.1
    update_score()
    instructions.clear()
    instructions.write("Press any arrow key to start!", align="center", font=("Arial", 16, "bold"))

# Function to update score display
def update_score():
    pen.clear()
    pen.write("YOUR SCORE: {}   HIGH SCORE: {}".format(score, high_score), align="center", font=("Times New Roman", 20, "bold"))

# Function for Game Over screen
def game_over():
    global high_score
    head.direction = "Stop"
    if score > high_score:
        high_score = score
    instructions.goto(0, 0)
    instructions.clear()
    instructions.write("Game Over! Your Score: {}\nClick to Play Again or Right Click to Exit".format(score), align="center", font=("Arial", 16, "bold"))

    # Add options to restart or exit
    win.onclick(start_new_game, 1)  # Left-click to restart
    win.onclick(exit_game, 3)  # Right-click to exit

# Function to start a new game
def start_new_game(x, y):
    instructions.clear()
    reset_game()
    win.onclick(None)  # Remove the restart/exit click event listeners

# Function to exit the game
def exit_game(x, y):
    win.bye()

# Main game loop
def main_game():
    global score, delay, high_score
    reset_game()  # Show initial message
    while True:
        win.update()
        if head.direction != "Stop":
            # Check for collision with border
            if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 390 or head.ycor() < -390:
                time.sleep(1)
                game_over()
                break

            # Check for collision with food
            if head.distance(food) < 20:
                x = random.randint(-370, 370)
                y = random.randint(-370, 370)
                food.goto(x, y)

                # Add new segment to the snake
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color(random.choice(['red', 'green', 'black', 'orange']))
                new_segment.penup()
                segments.append(new_segment)
                
                delay -= 0.001
                score += 10
                update_score()

            # Move snake segments in reverse order
            for i in range(len(segments) - 1, 0, -1):
                x = segments[i - 1].xcor()
                y = segments[i - 1].ycor()
                segments[i].goto(x, y)
            if segments:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x, y)
            
            # Move the snake
            move()

            # Check for collision with self
            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    game_over()
                    break

        time.sleep(delay)

# Start the game
main_game()
win.mainloop()
