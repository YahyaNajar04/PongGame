import turtle

wn = turtle.Screen()
wn.title("Pong Game by Yahya Najar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

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
Ball.shape("square")
Ball.color("red")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.06
Ball.dy = 0.06


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
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx = -0.06

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx = 0.06
