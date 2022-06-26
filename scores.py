
from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Arial"
FONT_SIZE = 15
FONT_TYPE = "normal"
POSITION = (0, 310)


class ScoreBoard(Turtle):
    """
    A class to manage the scores
    Children of the Turtle class
    
    Attributes
    ----------

    score : int
        current score 

    Methods
    -------
    write_score
        Write the current score on the screen
    """
    def __init__(self):
        super().__init__()
        self.shape("blank")
        self.penup()
        self.goto(POSITION)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))


