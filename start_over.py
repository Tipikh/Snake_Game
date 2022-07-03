
from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Arial"
POSITION = (0, 310)

class StartOver(Turtle):
    """
    A class to manage the starting and game-over screens
    
    Methods
    -------
    start_game
        Set up start screen

    game_over 
        Show game-over screen
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('blank')
        self.pencolor('black')
        self.speed("fastest")

    def start_game(self):
        """ Set up start screen """

        self.pensize(5)
        self.penup()
        self.goto(0, 100)
        self.pendown()
        self.write('Welcome to Snake !', align = 'center', font=(FONT_NAME, 24, 'normal'))
        self.penup()
        self.goto(0, 0)
        self.write("Press 'Enter' to start" , align= 'center', font=(FONT_NAME, 20, 'normal'))

    def game_over(self):
        """ Show game-over screen """

        self.goto(0, 30)
        self.write(f"GAME OVER", align='center', font=(FONT_NAME, 25, 'bold'))
        self.penup()
        self.goto(0, -30)
        self.write(f"Press 'Enter' to play again", align='center', font=(FONT_NAME, 15, 'normal'))


