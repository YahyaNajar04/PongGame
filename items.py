import turtle


class Paddle(turtle.Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)


class Ball(turtle.Turtle):
    def __init__(self, color, shape, x, y, sx, sy):
        super().__init__()
        self.speed(0)
        self.shape(shape)
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.dx = sx
        self.dy = sy
