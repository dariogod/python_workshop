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
# TODO

# Paddle B
# TODO

# Ball
# TODO

# Text: Score
# TODO


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
wn.onkeypress(quit, 'q')


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