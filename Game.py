import turtle
import winsound
from items import Paddle, Ball
from ScoreCard import Score
import time

wn = turtle.Screen()
wn.title("Pong Game by Yahya Najar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddles
paddle_A = Paddle("white", -350, 0)
paddle_B = Paddle("white", 350, 0)

# Ball
Ball = Ball("red", "circle", 0, 0, 0.1, 0.1)

# Tracking Score
score_a = 0
score_b = 0

# Making the Scoreboard
Score_Card = Score("white", 0, 260, "Player A: 0  Player B: 0", "center", font="Times New Roman", size=24,
                   fonttype="normal")

# Making Winning Screen
Win_A = turtle.Turtle()
Win_A.speed(0)
Win_A.color("green")
Win_A.penup()
Win_A.hideturtle()
Win_A.goto(0, 0)

Win_B = turtle.Turtle()
Win_B.speed(0)
Win_B.color("green")
Win_B.penup()
Win_B.hideturtle()
Win_B.goto(0, 0)


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


# Restarting the game
def restart_game():
    global score_a, score_b
    Ball.goto(0, 0)
    Ball.dx = 0.1
    Ball.dy = 0.1
    score_a = 0
    score_b = 0
    Score_Card.clear()
    Score_Card.write("Player A: 0  Player B: 0", align="center",
                     font=("Times New Roman", 24, "normal"))
    Win_A.clear()
    Win_B.clear()
    Ball.showturtle()
    wn.update()


# Main Game Loop
def update_game():
    global score_a, score_b
    while True:
        # Move the Ball
        Ball.setx(Ball.xcor() + Ball.dx)
        Ball.sety(Ball.ycor() + Ball.dy)

        # Border Checking
        if Ball.ycor() > 290:
            Ball.sety(290)
            Ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if Ball.ycor() < -290:
            Ball.sety(-280)
            Ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

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

        # Paddle Border
        if paddle_A.ycor() > 248:
            paddle_A.sety(248)

        if paddle_A.ycor() < -240:
            paddle_A.sety(-240)

        if paddle_B.ycor() > 248:
            paddle_B.sety(248)

        if paddle_B.ycor() < -240:
            paddle_B.sety(-240)

        # Paddle and Ball collision
        if (340 < Ball.xcor() < 350) and (
                paddle_B.ycor() + 40 > Ball.ycor() > paddle_B.ycor() - 40):
            Ball.setx(340)
            Ball.dx *= -1.175
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (-340 > Ball.xcor() > -350) and (
                paddle_A.ycor() + 40 > Ball.ycor() > paddle_A.ycor() - 40):
            Ball.setx(-340)
            Ball.dx *= -1.175
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if score_a == 5:
            Ball.dx = 0
            Ball.dy = 0
            Win_A.write("Player A wins \nr to restart", align="center", font=("Times New Roman", 24, "normal"))
            Ball.hideturtle()
            # winsound.PlaySound("Win.wav", winsound.SND_ASYNC)

        if score_b == 5:
            Ball.dx = 0
            Ball.dy = 0
            Win_B.write("Player B wins \nr to restart", align="center", font=("Times New Roman", 24, "normal"))
            Ball.hideturtle()
            # winsound.PlaySound("Win.wav", winsound.SND_ASYNC)
            wn.update()
            wn.ontimer(update_game, 10)


def start_game():
    wn.update()

    global score_a, score_b
    Ball.goto(0, 0)
    Ball.dx = 0.1
    Ball.dy = 0.1
    score_a = 0
    score_b = 0
    Score_Card.clear()
    Score_Card.write("Player A: 0  Player B: 0", align="center",
                     font=("Times New Roman", 24, "normal"))
    Win_A.clear()
    Win_B.clear()
    Ball.showturtle()
    update_game()


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(restart_game, "r")
wn.onkeypress(start_game, "e")

# Starting the game
start_game()

wn.ontimer(update_game, 10)

# Update Game
update_game()

wn.update()

wn.bye()