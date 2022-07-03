from turtle import Turtle
import random


class Food(Turtle):
    """
    A class to manage the snake's food
    
    Methods
    -------
    refresh
        Set the food in a random location
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.color('#FFD369')
        self.refresh()

    def refresh(self):
        """ Put the food in a random location """

        self.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))


