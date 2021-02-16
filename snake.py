from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.heading = 0
        self.createSnake()

    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.add_turtle(position)

    def add_turtle(self, position):
        turtle = Turtle(shape="square")
        turtle.color("yellow")
        turtle.penup()
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())


    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[i - 1].xcor()
            y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x, y)
        self.turtles[0].setheading(self.heading)
        self.turtles[0].forward(20)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.heading = UP

    def down(self):
        if self.turtles[0].heading() != UP:
            self.heading = DOWN

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.heading = LEFT

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.heading = RIGHT
