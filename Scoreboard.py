from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(arg=f"Score: {self.score}      High Score: {self.highscore}", align="center", font="Arial")

    def addscore(self):
        self.score += 1
        self.clear()
        self.updatescore()

    def resetGame(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file2:
                file2.write(str(self.highscore))

        self.score = 0
        self.updatescore()

    # def gameover(self):
    #     self.goto(x=0, y=20)
    #     self.write(arg="Game over", align="center", font="Arial")
    #

