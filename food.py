from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.color('chocolate')
        self.refresh()

    def refresh(self):
        self.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))


