import turtle
import os
import time

running = True

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

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

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Pen 2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, -280)
pen2.write("Press q to quit", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
        paddle_b.sety(y)

def quit():
    global running
    running = False

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(quit, "q")

# Main game loop
# Extra: laat het balletje sneller gaan
while running:
    time.sleep(0.005)
    
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        file = 'bounce.wav&'
        os.system("aplay -q " + file)
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay -q bounce.wav&")

    # Left and right
    if ball.xcor() > 400:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = ball.dx / abs(ball.dx)
        ball.dy = ball.dy / abs(ball.dy)
        ball.dx *= -1

    elif ball.xcor() < -400:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = ball.dx / abs(ball.dx)
        ball.dy = ball.dy / abs(ball.dy)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.dx < 0 and ball.xcor() < -330 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1.1
        os.system("aplay -q bounce.wav&")
    
    elif ball.dx > 0 and ball.xcor() > 330 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1.1
        os.system("aplay -q bounce.wav&")

wn.bye()