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
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over_text(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_score()
