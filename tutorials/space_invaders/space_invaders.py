# making space invaders using pygame and turtle module
import turtle
import os
import math
import random

# set up the screen
main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.title("Space Invaders")
main_screen.bgpic("space_invaders_background.gif")
main_screen.tracer(0)

main_screen.register_shape("invader.gif")
main_screen.register_shape("player.gif")

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

# initiate score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = f"Score: {score}"
score_pen.write(score_string, False, align="left", font=("Cambria", 14, "normal"))
score_pen.hideturtle()

# # create the player Turtle
player = turtle.Turtle()
player.color("green")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed = 0


number_enemies = 30
enemies = []

for i in range(number_enemies):
    enemies.append(turtle.Turtle())

enemy_start_x = -200
enemy_start_y = 250
enemy_number = 0


for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0


enemy_speed = 0.3


bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 7

# bullet state
bullet_state = "ready"

def move_left():
    player.speed = -3

def move_right():
    player.speed = 3

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280: # making sure triangle can't go off the screen
        x = -280
    if x > 280:
        x = 280
    player.setx(x) # take the current x, subtract the speed, and change the player's
    # location to the new x

def fire_bullet():
    global bullet_state # making a global variable - any changes within function are reflected here as well
    if bullet_state == "ready":
        os.system("afplay laser.wav&") # & stops it from pausing the programme
        bullet_state = "fire"
    # move bullet to just above the player
    x = player.xcor()
    y = player.ycor()
    bullet.setposition(x, y +10)
    bullet.showturtle()

def isCollision(t1, t2): # turtle 1, turtle 2
    distance = t1.distance(t2)
    if distance < 15:
        return True
    else:
        return False

# def play_sound(sound_file, time=0):
#     os.system(f"afplay {sound_file}")
#     if time > 0:
#         turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))

# create keyboard bindings
main_screen.listen() # listen for keyword actions
main_screen.onkeypress(move_left, "Left")
main_screen.onkeypress(move_right, "Right")
main_screen.onkeypress(fire_bullet, "space")

# play background music
# play_sound("background_music.mp3", 119) # makes my computer freeze?

# main game loop
while True:

    main_screen.update()
    move_player()

    for enemy in enemies:
    # move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # move enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1 # to make it go forward and back

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1 # doesn't go in loop as all enemies have same direction

        # check for collision between bullet and enemy
        if isCollision(bullet, enemy):
            os.system("afplay explosion.wav&")
            # reset the bullet
            bullet.hideturtle()
            bullet_state == "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            # x = random.randint(-200,200)
            # y = random.randint(100, 250)
            enemy.setposition(0, 10000)
            # update the score
            score += 10
            score_string = f"Score: {score}"
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Cambria", 14, "normal"))


        if isCollision(player, enemy):
            os.system("afplay explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!")
            break

    # move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # bullet reloads when reaches the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"


main_screen.mainloop()
