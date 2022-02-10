from turtle import Turtle


startpos = (0,-160)
movedis= 10
endplace= 160

class Player(Turtle):
    def __init__(self):
      super().__init__()
      self.shape("turtle")
      self.setheading(90)
      self.color("black")
      self.penup()
      self.cometostart()
  
    def cometostart(self):
      self.goto(startpos)

    def reached(self):
      if self.ycor()>=endplace:
        return True

    def move(self):
      self.forward(movedis)
 

