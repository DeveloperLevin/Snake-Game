from turtle import Turtle

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SPEED = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.pace = 0

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def add_segment(self, position):
        snake = Turtle('square')
        snake.color('black')
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def increase_speed(self):
        for i in range(len(self.segments)):
            if self.pace < len(SPEED):
                self.segments[i].speed(SPEED[self.pace])
            else:
                self.segments[i].speed(10)
        
        self.pace += 1
        
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)