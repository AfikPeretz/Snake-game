from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('My Snake Game')
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        score_board.update()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        is_game_on = False
        score_board.game_over()

    for i in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[i]) < 10:
            is_game_on = False
            score_board.game_over()



screen.exitonclick()