from turtle import Turtle

SNAKE_STARTCOR = [(0, 0), (-20, 0), (-40, 0)]# Tuple that stores the coordinates of the different turtles/snake body
SNAKE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snakes = []  # list of all the growing snake body pieces
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for s in SNAKE_STARTCOR:
            self.addsnakebody(s)

    def addsnakebody(self, s):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(s)
        self.snakes.append(snake)

    def resetsnake(self):
        for snake in self.snakes:
            snake.goto(10000, 10000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def extend(self):
        self.addsnakebody(self.snakes[-1].position())

    def move(self):#self allows me to reference the variables in this class
        for snakebody in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[snakebody-1].xcor()
            new_y = self.snakes[snakebody-1].ycor()
            self.snakes[snakebody].goto(new_x, new_y)
        self.head.forward(SNAKE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)








#Snake Game note :
# The movement of all the parts of the snake continously
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#