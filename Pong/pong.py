import turtle
import os
import time

### Variables ###

# Game Loop
running = True

# Score
# TODO


### Turtles ###

# Window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Text: Score
txt_score = turtle.Turtle()
txt_score.speed(0)
txt_score.shape("square")
txt_score.color("white")
txt_score.penup()
txt_score.hideturtle()
txt_score.goto(0, 260)
txt_score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


### Functions ###

def paddle_a_up():
    # TODO
    pass

def paddle_a_down():
    # TODO
    pass

def paddle_b_up():
    # TODO
    pass

def paddle_b_down():
    # TODO
    pass

def quit():
    global running
    running = False


### Keyboard bindings ###

wn.listen()
wn.onkeypress(quit, "q")
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


### Main game loop ###

while running:    
    wn.update()
    
    # Move the ball
    # TODO

    ## Border checking ##

    # Top
    # TODO

    # Bottom
    # TODO

    # Left
    # TODO

    # Right
    # TODO

    ## Paddle and ball collisions ##

    # Left
    # TODO
    
    # Right
    # TODO

wn.bye()