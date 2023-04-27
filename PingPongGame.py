# ping pong game

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Volibear")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Volibear:0   Riven:0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_A.ycor()
    y += 40
    paddle_A.sety(y)


def paddle_a_down():
    y = paddle_A.ycor()
    y -= 40
    paddle_A.sety(y)

def paddle_b_up():
    y = paddle_B.ycor()
    y += 60
    paddle_B.sety(y)


def paddle_b_down():
    y = paddle_B.ycor()
    y -= 60
    paddle_B.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("sectionpass.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("sectionpass.wav", winsound.SND_ASYNC)

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx * -1
        score_a += 1
        pen.clear()
        pen.write("Volibear: {} Riven: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("sectionpass.wav", winsound.SND_ASYNC)

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx * -1
        score_b += 1
        pen.clear()
        pen.write("Volibear: {} Riven B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("sectionpass.wav", winsound.SND_ASYNC)

    if paddle_A.ycor() > 270:
        paddle_A.sety(270)

    if paddle_A.ycor() < -270:
        paddle_A.sety(-270)

    if paddle_B.ycor() > 270:
        paddle_B.sety(270)

    if paddle_B.ycor() < -270:
        paddle_B.sety(-270)

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 50 and ball.ycor() > paddle_B.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("sectionpass.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 50 and ball.ycor() > paddle_A.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("sectionpass.wav", winsound.SND_ASYNC)


