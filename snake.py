from turtle import Turtle

MOVEMENT_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))


class Snake:
    """
    A class to show and manage the behavior of the snake
    Children of the Turtle class
    
    The snake is composed of several segments. Each segment is an 
    instance of the Turtle class and has a square shape of size 20. 
    Each segment is associated to a tuple that give the position of 
    that segment 

    When the snake eat some food a new segment is added 

    Attributes
    ----------

    direction : int
        the direction in which the snake is heading

    segments : list of instances of the Turtle class
        the different snake's parts    

    head : instance of the Turtle class 
        the first segment of the snake


    Methods
    -------
    create_snake
        create the snake by adding a segment for each snake's positions

    add_segment
        create a new segment at the given position
    """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = None

    def create_snake(self):
        """ 
        Create the snake by adding a segment for each snake's positions 
        """
        
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """ 
        Create a new segment at the given position and add it to the 
        list of segments 

        Parameters : 
        ------------
        position : tuple
            the position of the segment
        """

        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('chocolate')
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def grow_up(self):
        """ 
        Add a new segment at the end of the snake
        """        
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Make the snake move to the next position.
        
        The head is moving forward and then each segment goes 
        to the position of the previous segment. 
        """
        for i in reversed(range(1, len(self.segments))):
            position = self.segments[i - 1].pos()
            self.segments[i].goto(position)

        self.segments[-1].showturtle()
        self.head.forward(MOVEMENT_DISTANCE)

    def set_direction(self, direction):
        """ Set the direction attribute of the snake """
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