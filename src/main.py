import turtle
import winsound
import paddle
import Ball

#--window screen section--
window = turtle.Screen()
window.title("The Pingpong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

ball = Ball.Ball()
paddle_1 = paddle.Paddle(-350)
paddle_2 = paddle.Paddle(350)

#Score section
score_1 = 0
score_2 = 0


#==Pen==
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {score_1}  Player B: {score_2}", align="center", font=("Courier", 24, "normal"))


#keyboard Input
window.listen()
window.onkeypress(paddle_1.move_up, "w")
window.onkeypress(paddle_1.move_down,"s")
window.onkeypress(paddle_2.move_up,"Up")
window.onkeypress(paddle_2.move_down,"Down")



# Loop game
while True:
    window.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border setting
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Set the game resetting boundy
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write(f"Player A: {score_1}  Player B: {score_2}", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < - 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write(f"Player A: {score_1}  Player B: {score_2}", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #--Paddle and ball collisions--
        #Right paddle
    if (-340 > ball.xcor() > -350) and (paddle_1.ycor() + 40 > ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        #Left paddle
    if (340 < ball.xcor() < 350) and (paddle_2.ycor() + 40 > ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    #AI player
    if paddle_2.ycor() < ball.ycor() and abs(paddle_2.ycor() - ball.ycor()) > 20:
        paddle_2.move_up()
    elif paddle_2.ycor() > ball.ycor() and abs(paddle_2.ycor() - ball.ycor()) < 20:
        paddle_2.move_down()


