import turtle

class Ball:
    def __init__(self):
        # ==Ball==
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.dx = 0.1
        self.dy = 0.1

    def xcor(self):
        return self.turtle.xcor()
    def ycor(self):
        return self.turtle.ycor()
    def setx(self,x):
        return self.turtle.setx(x)
    def sety(self,y):
        return self.turtle.sety(y)
    def goto(self,x,y):
        return self.turtle.goto(x,y)
