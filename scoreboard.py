from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as file:
                file.write(f'{self.high_score}')
        self.score = -1
        self.update()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color('red')
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
