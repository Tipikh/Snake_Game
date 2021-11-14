from turtle import Turtle


ALIGNMENT = "center"
FONT_NAME = "Arial"
FONT_SIZE = 15
FONT_TYPE = "normal"
POSITION = (0, 310)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("blank")
        self.penup()
        self.goto(POSITION)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.goto(0, 30)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT_NAME, 25, 'bold'))
        self.penup()
        self.goto(0, -30)
        self.write(f"Press 'Enter' to play again", align=ALIGNMENT, font=(FONT_NAME, 15, 'normal'))

    def restart(self):
        self.clear()
        self.shape("blank")
        self.penup()
        self.goto(POSITION)
        self.score = 0
        self.write_score()

