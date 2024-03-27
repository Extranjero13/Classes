import turtle
import random
import math

#Screen Settings
screen = turtle.Screen()          # for screen (window)
screen.setup(500, 500)
screen.tracer(0)
screen.bgcolor('Blue')# tell screen to not show automatically

#Tank draw settings
tank = turtle.Turtle()
tank.speed(0)                 # draw as fast as possible
tank.width(4)                    # line thickness
                                

#enemy tank initialization
enemy_tank1 = turtle.Turtle()
enemy_tank1.speed(0)  # Draw as fast as possible
enemy_tank1.width(4)  # Line thickness

enemy_tank2 = turtle.Turtle()
enemy_tank2.speed(0)  # Draw as fast as possible
enemy_tank2.width(4)  # Line thickness

#initial positions for enemy tanks
enemy_tank1.goto(-100, 0)
enemy_tank2.goto(100, 0)

turret_angle = 0

def draw_tank(tank):
    tank.clear()
    # Draw the line inside the circle
    tank.dot(50,"green")
    tank.forward(30)            #turret draw
    tank.backward(30)
    screen.update()
    tank.setheading(turret_angle)
    tank.pendown()
    tank.forward(30)
    tank.penup()
    tank.goto(x, y)
    screen.update()

x = 0
y = 0
angle = 0
velocity = 5

def draw_enemy_tank(enemy_tank, color):
    enemy_tank.clear()
    enemy_tank.dot(50, "red")
    enemy_tank.forward(30)     # enemy turret draw
    enemy_tank.backward(30)
    screen.update()


def movement(angle, velocity):

    angle = math.radians(angle)

    dx = velocity * math.cos(angle)
    dy = velocity * math.sin(angle)

    return dx, dy

def move():
     global x, y,angle
     dx, dy = movement(angle, velocity)
     new_x, new_y = x + dx, y + dy
    
    # Check for collisions
     if not collision(new_x, new_y):
        x, y = new_x, new_y
     else:
        angle +=90
        dx, dy = movement(angle, velocity)
        x, y = x + dx, y + dy
        tank.goto(x, y)
        draw_tank(tank)
   
           


def up():
    global angle
    angle = turret_angle                                
    move()

def down():
    global angle
    angle = turret_angle + 180
    move()

def left():
    global turret_angle
    turret_angle += 10
    draw_tank(tank)

def right():
    global turret_angle
    turret_angle -= 10
    draw_tank(tank)

def update_enemy_movement():
    for enemy_tank in [enemy_tank1, enemy_tank2]:
        # angle calculations
        dx = x - enemy_tank.xcor()
        dy = y - enemy_tank.ycor()
        angle_to_player = math.atan2(dy, dx)
        angle_to_player_degrees = math.degrees(angle_to_player)

        # draws enemy tank at new position
        draw_enemy_tank(enemy_tank, "red")

        # sets orientation
        enemy_tank.setheading(angle_to_player_degrees)

        # move the enemy tank towards the player (speed)
        enemy_tank.forward(2)  

    # delay to update movement of enemy tanks
    screen.ontimer(update_enemy_movement, 250)

def collision(new_x,new_y): 
        #screen collision detection
       if abs(new_x) >= screen.window_width() / 2 or abs(new_y) >= screen.window_height() / 2:
        return True
            #(xb - xa)^2 + (yb - ya)^2 <= (ra + rb)^2
       distance_between_1 = math.sqrt((new_x - enemy_tank1.xcor())**2 + (new_y - enemy_tank1.ycor())** 2)               #Static Circle-Circle collison detection. sqrt(Change of x)^2 + sqrt(change of y)^2
       distance_between_2 = math.sqrt((new_x - enemy_tank2.xcor())**  2 + (new_y - enemy_tank2.ycor()) ** 2)
       collide_dis = 60

       if distance_between_1 < collide_dis or distance_between_2 < collide_dis:             #compare distance and radii of circles to determine collision
            return True

       return False
                
def show_dist():
    distance1 = int(enemy_tank1.distance(x, y))              #distance for tank 1
    distance2 = int(enemy_tank2.distance(x, y))              #distance for tank 2 
    print("Distance to Enemy Tank 1: ", distance1, "m")
    print("Distance to Enemy Tank 2: ", distance2, "m")
    screen.ontimer(show_dist, 1500)  #this will constantly update the screen with a recursive call, 1500 ms delay
    

    units=[distance1,distance2]         #selection sort, place the enemy tank distances into a list
    for i in range(len(units)):                 #We use a for loop with the range function so as to avoid float and integer confusion
        small=i                                     #initialize small variable which will hold the current minumum value
        for j in range(i+1,len(units)):             # we use i+1 to check the next value in the list 
            if units[j] < units[small]:
                small=j
        units[i],units[small]=units[small],units[i]     #Swap positions
    print("Enemy Tank 1 is : ", units[0], "m away from player");
    print("Enemy Tank 2 is : ", units[1], "m away from player");
    
    




    
turtle.listen()
turtle.onkeypress(down, "Down")
turtle.onkeyrelease(down, "Down")
turtle.onkeypress(up, "Up")
turtle.onkeyrelease(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeyrelease(left,"Left")
turtle.onkeypress(right, "Right")
turtle.onkeyrelease(right,"Right")


draw_tank(tank)

update_enemy_movement()

show_dist()
screen.update()

turtle.mainloop()

