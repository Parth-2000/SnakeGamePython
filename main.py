from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(width=600, height=600)

screen.bgcolor("black")

screen.title("Snake Game")

screen.tracer(0)

snake = Snake()

food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or \
            snake.turtles[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if head collides with any segments in the tail
    # Trigger game over

    for segment in snake.turtles[1:]:
        # if segment == snake.turtles[0]:
        #     pass
        # elif snake.turtles[0].distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()
        if snake.turtles[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
