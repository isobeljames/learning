# making space invaders using pygame and turtle module
import turtle
import os
import math

# set up the screen
main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.title("Space Invaders")

# draw border
border_pen = turtle.Turtle()
border_pen.speed(0) # 0 is actually the fastest
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# # create the player Turtle
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

# create enemy

enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemy_speed = 2

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20

# bullet state
bullet_state = "ready"

def move_left():
    x = player.xcor() # current player's coordinates
    x -= player_speed
    if x < -280: # making sure triangle can't go off the screen
        x = -280
    player.setx(x) # take the current x, subtract the speed, and change the player's
    # location to the new x
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bullet_state # making a global variable - any changes within function are reflected here as well
    if bullet_state == "ready":
        bullet_state = "fire"
    # move bullet to just above the player
    x = player.xcor()
    y = player.ycor()
    bullet.setposition(x, y +10)
    bullet.showturtle()

def isCollision(t1, t2): # turtle 1, turtle 2
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow)
    if distance < 15:
        return True
    else:
        return False

# create keyboard bindings
turtle.listen() # listen for keyword actions
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")

# main game loop
while True:

    # move the enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # move enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1 # to make it go forward and back
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    # move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # bullet reloads when reaches the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

    # check for collision between bullet and enemy
    if isCollision(bullet, enemy):
        # reset the bullet
        bullet.hideturtle()
        bullet_state == "ready"
        bullet.setposition(0, -400)
        # reset the enemy
        enemy.setposition(-200, -250)


    enemy.setx(x)

delay = input("Press enter to finish.")
