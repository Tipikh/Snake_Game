from turtle import Turtle

MOVEMENT_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = None

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('chocolate')
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def grow_up(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in reversed(range(1, len(self.segments))):
            position = self.segments[i - 1].pos()
            self.segments[i].goto(position)

        self.segments[-1].showturtle()
        self.head.forward(MOVEMENT_DISTANCE)

    def get_direction(self, direction):
        self.direction = direction

    def go_up(self, event):
        if self.head.heading() != DOWN:
            if self.direction != DOWN:
                self.head.setheading(UP)

    def go_down(self, event):
        if self.head.heading() != UP:
            if self.direction != UP:
                self.head.setheading(DOWN)

    def go_left(self, event):
        if self.head.heading() != RIGHT:
            if self.direction != RIGHT:
                self.head.setheading(LEFT)

    def go_right(self, event):
        if self.head.heading() != LEFT:
            if self.direction != LEFT:
                self.head.setheading(RIGHT)


    def hide_snake(self):
        for segment in self.segments:
            segment.hideturtle()

    def show_snake(self):
        for segment in self.segments:
            segment.showturtle()