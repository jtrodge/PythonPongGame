#Pong Game (Non-Object oriented style)
#python3
# turtle is great for simple games
# pygame is great for advanced games
import turtle

win = turtle.Screen()
win.title("Jason's Pong Game \U0001f600")
win.bgcolor("red")
# 0, 0 is middle of Screen
# +400 right, -400 left
# +300 top, -300 bottom
win.setup(width=800, height=600)
# stops the window from updating
# speeds up the game
win.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
# turtle object
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
# stretch shape
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
# stretch shape
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
# change in the speed of the ball
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    # returns paddle a y coordinate
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    # returns paddle a y coordinate
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    # returns paddle a y coordinate
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    # returns paddle a y coordinate
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
win.listen() # listen to keyboard input
win.onkeypress(paddle_a_up, "Up")
win.onkeypress(paddle_a_down, "Down")
win.onkeypress(paddle_b_up, "a")
win.onkeypress(paddle_b_down, "s")



# Main game loop
while True:
    # updates screen everytime everytime loop runs
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        # Reverses direction
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        # Reverses direction
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
