from turtle import Turtle
import random

colours = ["red", "deeppink", "yellow", "aqua", "blue", "purple","lawngreen"]
starting_speeddis = 5
next_speed = 6

class car:
  def __init__(self):
    self.allcars=[]
    self.carspeed=starting_speeddis
    #  super().__init__()
  
  def createcar(self):
    random_chance=random.randint(1,6)
    if random_chance==1:
      new=Turtle("square")
      new.penup()
      new.color(random.choice(colours))
      new.shapesize(1,2)

      randy=random.randint(-120,120)
      new.goto(200,randy)
      self.allcars.append(new)
  
  def movecar(self):
    for eachcar in self.allcars:
      eachcar.backward(self.carspeed)

  def speedup(self):
    self.carspeed+= next_speed
    self.movecar()
    





   
