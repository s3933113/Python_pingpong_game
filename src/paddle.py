import turtle

class Paddle:
    def __init__(self,x):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.shapesize(stretch_wid=5, stretch_len=1)
        self.turtle.goto(x, 0)

    def move_up(self):
        self.turtle.sety(self.turtle.ycor() + 5)

    def move_down(self):
        self.turtle.sety(self.turtle.ycor() - 5)

    def xcor(self):
        return self.turtle.xcor()

    def ycor(self):
        return self.turtle.ycor()