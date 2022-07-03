
from turtle import Turtle

LIMIT = 291


class Limits(Turtle):
    """
    A class to manage the game's limits
    
    Methods
    -------
    create_limits
        Create the limits of the game
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('blank')
        self.goto(-316, -315)
        self.pencolor('black')
        self.speed("fastest")

    def create_limits(self):
        """Create the limits of the game"""

        self.pensize(1)
        self.goto(-1 * LIMIT, -1 * LIMIT)
        self.pendown()
        self.goto(LIMIT, -1 * LIMIT)
        self.goto(LIMIT, LIMIT)
        self.goto(-1 * LIMIT, LIMIT)
        self.goto(-1 * LIMIT, -1 * LIMIT)


