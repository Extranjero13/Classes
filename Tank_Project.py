import turtle
import random
import math

#Screen Settings
screen = turtle.Screen()          # for screen (window)
screen.setup(500, 500)
screen.tracer(0)             # tell screen to not show automatically

#Tank draw settings
tank = turtle.Turtle()
tank.speed(0)                 # draw as fast as possible
tank.width(4)                    # line thickness
           # hide the turtle


def draw_tank(tank):
    tank.clear()
    # Draw the line inside the circle
    tank.dot(50,"green")
    tank.forward(30)            #turret draw
    tank.backward(30)
    screen.update()

x = 0
y = 0
angle = 0
velocity = 5
adelante=False     #Boolean for key press, false= no go. True = go
patras=False

def forward():
    global adelante
    adelante = True
    move()

def no_forward():
    global adelante
    adelante=False

def motion():               #Function to keep the turtle moving
    if adelante:
        tank.forward(10)
        screen.ontimer(move,10)

def backwards():
    global patras
    patras = True
    move()

def no_backward():
    global patras
    patras=False

def opp_motion():
    if patras:
        tank.backward(10)
        
        screen.ontimer(move,10)



def movement(angle, velocity):

    angle = math.radians(angle)

    dx = velocity * math.cos(angle)
    dy = velocity * math.sin(angle)

    return dx, dy

def move():
    global x, y
    dx, dy = movement(angle, velocity)

    x += dx
    y += dy

    tank.goto(x, y)
    draw_tank(tank)


def down():
    global angle
    angle = 270
    move()

def up():
    global angle
    angle = 90
    move()

def left():
    global angle
    angle = 180
    tank.left(10)
    move()

def right():
    global angle
    angle = 0
    tank.right(10)
    move()




turtle.listen()
turtle.onkeypress(down, "Down")
turtle.onkeyrelease(down, "Down")
turtle.onkey(up, "Up")
turtle.onkeyrelease(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeyrelease(left,"Left")
turtle.onkeypress(right, "Right")
turtle.onkeyrelease(right,"Right")


draw_tank(tank)

screen.update()

turtle.mainloop()



