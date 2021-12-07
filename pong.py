import turtle as t
playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# paddles
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# the ball

ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection = 0.2
ballydirection = 0.2

# the pen

pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=("Courier", 24, "normal"))

# moveing left paddle

def leftPaddleUp():
    y = leftPaddle.ycor()
    y = y+90 
    leftPaddle.sety(y)

def leftPaddleDown():
    y = leftPaddle.ycor()
    y = y-90
    leftPaddle.sety(y)

def rightPaddleUp():
    y = rightPaddle.ycor()
    y = y+90
    rightPaddle.sety(y)

def rightPaddleDown():
    y = rightPaddle.ycor()
    y = y-90
    rightPaddle.sety(y)

# keyboard binding to play game

window.listen()
window.onkeypress(leftPaddleUp, "w")
window.onkeypress(leftPaddleDown, "s")
window.onkeypress(rightPaddleUp, "Up")
window.onkeypress(rightPaddleDown, "Down")

while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(5,5)
        ballxdirection = ballxdirection * -1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("score: {}".format(playerAscore), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(5,5)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("score: {}".format(playerBscore), align="center", font=("Courier", 24, "normal"))

    # paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < leftPaddle.ycor() + 50 and ball.ycor() > leftPaddle.ycor() - 50):
        ballxdirection = ballxdirection * -1
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < rightPaddle.ycor() + 50 and ball.ycor() > rightPaddle.ycor() - 50):
        ballxdirection = ballxdirection * -1

    # game over
    if playerAscore == 10:
        pen.clear()
        pen.write("Player A wins", align="center", font=("Courier", 24, "normal"))
        break
    if playerBscore == 10:
        pen.clear()
        pen.write("Player B wins", align="center", font=("Courier", 24, "normal"))
        break

    
