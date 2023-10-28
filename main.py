from turtle import Screen
from snake_CLass import Snake
from food import Food
from Scoreboard import Scoreboard
import time

GameIsOn = True
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while GameIsOn:
    screen.update()#
    time.sleep(0.1)#
    snake.move()
#Detect food and collision with snake

    if snake.head.distance(food) < 20:
        food.refresh()
        score.addscore()
        snake.extend()

#Detec collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.resetGame()
        snake.resetsnake()

# Detect collison with tail :
for snakeb in snake.snakes:
    if snakeb == snake.head:
        pass
    elif snake.head.distance(snakeb) < 10:
        score.resetGame()
        snake.resetsnake()


screen.exitonclick()
