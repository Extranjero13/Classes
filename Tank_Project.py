import turtle

# Screen Settings
screen = turtle.Screen()          # for screen (window)
screen.setup(500, 500)
screen.tracer(0)             # tell screen to not show automatically

# Tank draw settings
tank = turtle.Turtle()
tank.speed(0)                 # draw as fast as possible
tank.width(4)                    # line thickness
tank.hideturtle()             # hide the turtle
head= turtle.Turtle()
head.speed(0)
head.width(2)
head.hideturtle()

def draw_tank():
    r=25
    for side in range(4):    # draw a square using a for loop, 3 turns so range = 4. Side is a variable (i)
        tank.forward(100)    #width of tank object (square)
        tank.left(90)
        for i in range(4):
            head.circle(r)
            head.goto(tank.xcor()-50,tank.ycor()-50)
       
    


# Tank moving commands
def down():
    tank.setheading(270)
    tank.forward(10)
    head.setheading(270)
    head.forward(10)
def up():
    tank.setheading(90)
    tank.forward(10)
    head.setheading(90)
    head.forward(10)
def left():
    tank.setheading(180)
    tank.forward(10)
    head.setheading(180)
    tank.forward(10)

def right():
    tank.setheading(0)
    tank.forward(10)
    head.setheading(0)
    head.forward(10)

turtle.listen()                 # Begin listening for arrow key commands
turtle.onkey(down, "Down")      # Sets up instructions for keystrokes
turtle.onkey(up, "Up") 
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

# Execute main loop/ tank moving
while True:
    tank.clear()
    head.clear()
    draw_tank()
    screen.update()



  


