
import time
from turtle import Turtle,Screen
from player import Player
from car_manager import car

sir=Turtle()
sir.hideturtle()
sir.penup()
sir.goto(-180,160)
sir.write("level 1")


screen = Screen()
screen.title("Cross The Traffic")
screen.setup(width=400, height=390)
screen.tracer(0)

me=Player()
carss=car()

screen.listen()
screen.onkey(me.move,"Up")

num=1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carss.createcar()
    carss.movecar()

    for car in carss.allcars:
      if car.distance(me)<20:
        sir.goto(0,0)
        sir.write("Game Over",align="center",font=["arial",20,"normal"])
        
        game_is_on=False

      if me.reached():
        sir.clear()
        me.cometostart()
        sir.goto(-180,160)
        num+=1
        sir.write(f"Level {num}")
        carss.speedup()




screen.exitonclick()