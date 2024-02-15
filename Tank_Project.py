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
    tank.left(18)
    move()

def right():
    global angle
    angle = 0
    tank.right(18)
    move()




turtle.listen()
turtle.onkey(down, "Down")
turtle.onkey(up, "Up")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")


draw_tank(tank)

screen.update()

turtle.mainloop()



