from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        #adds labbels to the top of the page that displays scores and high score
        self.score = 0
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.write(f"Score : {self.score}", align="center", font=("Times new Roman", 24, "bold"))


    def dis(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Times new Roman", 24, "bold"))
        
    def lost(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Times new Roman", 24, "bold"))

