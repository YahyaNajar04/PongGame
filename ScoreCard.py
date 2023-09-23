import turtle


class Score(turtle.Turtle):
    def __init__(self, color, text, align, font, size, fonttype):
        super().__init__()
        self.speed(0)
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(text, align=align, font=(font, size, fonttype))
