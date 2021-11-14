from turtle import Turtle

LIMIT = 291


class Limits(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('blank')
        self.goto(-316, -315)
        self.pencolor('black')
        self.speed("fastest")

    def create_limits(self):
        self.pensize(1)
        self.goto(-1 * LIMIT, -1 * LIMIT)
        self.pendown()
        self.goto(LIMIT, -1 * LIMIT)
        self.goto(LIMIT, LIMIT)
        self.goto(-1 * LIMIT, LIMIT)
        self.goto(-1 * LIMIT, -1 * LIMIT)

    def start_game(self):
        self.pensize(5)
        self.penup()
        self.goto(0, 100)
        self.pendown()
        style = ('Arial', 24, 'normal')
        self.write('Welcome to Snake !', align = 'center', font=style)

        self.penup()
        self.goto(0, 0)
        self.write("Press 'Enter' to start" , align= 'center', font=('Arial', 20, 'normal'))

    def hide_start(self):
        self.clear()
        self.create_limits()




