from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.penup()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0

    def score_increase(self):
        self.score += 1
        self.update_score()


