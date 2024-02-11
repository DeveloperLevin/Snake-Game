from turtle import Turtle, Screen, title
from main import Snake
from food import Food
from score import Score
#from playsound import playsound
import winsound
import random as rd
import time

#set screen object with a background color
screen = Screen()
screen.setup(500, 500)
screen.bgcolor('green')

#screen title
Screen_title = title("Snake Game")

def random():
    return rd.randint(-240, 240)

point = 0

#Turns animation off, only changes when we call the update method
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

#functions to move the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.listen()
is_game_on = True
#playsound('game-start.mp3')
#Condition to begin the game
while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Detect collision with food using distance
    if snake.head.distance(food) < 15:
        #playsound('blip.mp3')
        winsound.Beep(2000, 100)
        snake.extend()
        snake.increase_speed()
        score.dis()
        food.refresh()

    #Detect wall collision
    if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        #playsound('negative_beeps.mp3')
        is_game_on = False
        score.lost()

    #Detect tail collision
    for segment in snake.segments:
        #bypasses the snaks head
        if segment == snake.head:
            continue

        if snake.head.distance(segment) < 10:
            #playsound('negative_beeps.mp3')
            is_game_on = False
            score.lost()
    

screen.mainloop()
screen.exitonclick()