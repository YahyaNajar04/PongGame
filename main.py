import turtle

wn = turtle.Screen()
wn.title("Pong Game by Yahya Najar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Tracking Score
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
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("red")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.1
Ball.dy = 0.1

# Making the Scoreboard
Score_Card = turtle.Turtle()
Score_Card.speed(0)
Score_Card.color("white")
Score_Card.penup()
Score_Card.hideturtle()
Score_Card.goto(0, 260)
Score_Card.write("Player A: 0  Player B: 0", align="center", font=("Times New Roman", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)


def paddle_a_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)


def paddle_b_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


def paddle_b_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move the Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border Checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-280)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx = -0.06
        score_a += 1
        Score_Card.clear()
        Score_Card.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                         font=("Times New Roman", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx = 0.06
        score_b += 1
        Score_Card.clear()
        Score_Card.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                         font=("Times New Roman", 24, "normal"))

    # Paddle and Ball collision
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (
            Ball.ycor() < paddle_B.ycor() + 40 and Ball.ycor() > paddle_B.ycor() - 40):
        Ball.setx(340)
        Ball.dx *= -1.5

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (
            Ball.ycor() < paddle_A.ycor() + 40 and Ball.ycor() > paddle_A.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1.5
