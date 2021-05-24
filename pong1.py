import turtle
import os

wn = turtle.Screen()
wn.title("Pong by Mayur Chakalasiya")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)



# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5  # pixel move 2 pixels
ball.dy = -0.5  # pixel move 2 pixels

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0 Player B:0", align="Center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0


# Paddle up and down
def paddle_a_up():
    y = paddle_a.ycor()
    if paddle_a.ycor() < 240:
        y += 20
    paddle_a.sety(y)


def paddle_a_dw():
    y = paddle_a.ycor()
    if paddle_a.ycor() > -240:
        y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if paddle_b.ycor() < 240:
        y += 20
    paddle_b.sety(y)


def paddle_b_dw():
    y = paddle_b.ycor()
    if paddle_b.ycor() > -240:
        y -= 20
    paddle_b.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_dw, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_dw, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Board checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        os.system("aplay bounce.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        os.system("aplay bounce.wav&")

    # Update score on screen
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="Center", font=("Courier", 24, "normal"))

    # Paddle and Ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    # Paddle and Ball collisions
    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
