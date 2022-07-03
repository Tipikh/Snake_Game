from turtle import Screen
from snake import Snake
from scores import ScoreBoard
from limits import Limits
from food import Food
from start_over import StartOver
import time
from math import sqrt

BOARD_LIMIT = 281


def collision(tail, head):
    """ A function to check for collisions between head and tail """
    
    y_tail = tail.ycor()
    x_tail = tail.xcor()
    y_head = head.ycor()
    x_head = head.xcor()

    distance = round(sqrt((x_head - x_tail) ** 2 + (y_head - y_tail) ** 2), 2)

    if distance < 10:
        return True
    else:
        return False


def game(event):

    global screen
    global canvas
    global limit
    global start_over
    global score

    # Initialise snake, limits, food and score
    snake = Snake()
    start_over.clear()
    food = Food()
    score.score = 0
    score.clear()
    score.write_score()

    # Key binding
    canvas.bind('<Up>', snake.go_up)
    canvas.bind('<Down>', snake.go_down)
    canvas.bind('<Left>', snake.go_left)
    canvas.bind('<Right>', snake.go_right)
    
    game_is_on = True
    
    # Set initial speed (time between to snake moves)
    speed = 0.15
    
    while game_is_on:

        snake.move()
        
        # Set time to wait before next move
        time.sleep(speed)
        
        snake.set_direction(snake.head.heading())
        
        # Check for collision between snake head and food
        if snake.head.distance(food) < 1:
            snake.grow_up()
            food.refresh()
            food_on_snake = True
            
            # This while loop ensures that the new generated food
            # does not fall on snake's body 
            while food_on_snake:
                count = 0
                for segment in snake.segments:
                    if abs(food.xcor() - segment.xcor()) < 11 and \
                        abs(food.ycor() - segment.ycor()) < 11:
                            
                        food.refresh()
                        count += 1
                if count == 0:
                    food_on_snake = False

            # Increase speed and score
            speed *= 0.97
            score.score += 1
            score.clear()
            score.write_score()

        # Check if snake collide with board limits
        if snake.head.xcor() > BOARD_LIMIT or \
            snake.head.xcor() < BOARD_LIMIT * -1 or \
                snake.head.ycor() > BOARD_LIMIT or \
                    snake.head.ycor() < BOARD_LIMIT * -1:
                        
            game_is_on = False

        # Check if snake collide with himself
        for segment in snake.segments[1:]:
            if collision(segment, snake.head):
                
                game_is_on = False

        # Show game over screen 
        if not game_is_on:
            snake.hide_snake()
            food.hideturtle()
            start_over.game_over()
            
        screen.update()


if __name__ == '__main__':

    screen = Screen()
    screen.setup(width=700, height=720)
    screen.bgcolor('#EEEEEE')
    screen.title("Snake")

    # Prevent the screen from refreshing unless said explicitly with update()
    screen.tracer(0)
    screen.update()

    start_over = StartOver()
    limit = Limits()
    limit.create_limits()
    score = ScoreBoard()
    start_over.start_game()

    screen.listen()
    canvas = screen.getcanvas()

    # Execute "game" function when the user press Enter
    canvas.bind('<Return>', game)

    screen.update()
    screen.exitonclick()
