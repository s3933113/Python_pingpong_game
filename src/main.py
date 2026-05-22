import turtle

#--window screen section--
window = turtle.Screen()
window.title("The Pingpong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# ==Paddle 1==
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

# ==Paddle 2==
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

#==Ball==
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)


#==Function==

#Paddle_1 section
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

#Paddle_2 section
def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

#keyboard Input
window.listen()
window.onkeypress(paddle_1_up,"w")
window.onkeypress(paddle_1_down,"s")
window.onkeypress(paddle_2_up,"Up")
window.onkeypress(paddle_2_down,"Down")



# Loop game
while True:
    window.update()
