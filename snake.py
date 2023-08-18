from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        #self.head.setheading(90) one line will work
        if self.head.heading() == 0:
            self.head.setheading(UP)
        elif self.head.heading() == 180:
            for i in range(len(self.segments)):
                self.segments[i].right(UP)

    def down(self):
        if self.head.heading() == 0:
            for i in range(len(self.segments)):
                self.segments[i].right(90)
        elif self.head.heading() == 180:
            for i in range(len(self.segments)):
                self.segments[i].left(90)

    def left(self):
        if self.head.heading() == 90:
            for i in range(len(self.segments)):
                self.segments[i].left(90)
        elif self.head.heading() == 270:
            for i in range(len(self.segments)):
                self.segments[i].right(90)

    def right(self):
        if self.head.heading() == 90:
            for i in range(len(self.segments)):
                self.segments[i].right(90)
        elif self.head.heading() == 270:
            for i in range(len(self.segments)):
                self.segments[i].left(90)
