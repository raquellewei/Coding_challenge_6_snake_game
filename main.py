from turtle import Screen
from snake import Snake
import time
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


game_on = True

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food


screen.exitonclick()