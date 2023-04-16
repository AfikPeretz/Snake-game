from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.size = 3
        self.start_pos_x = 0
        self.start_pos_y = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(self.size):
            self.add_segment(self.start_pos_x, self.start_pos_y)

    def add_segment(self, start_pos_x, start_pos_y):
        new_snake_segment = Turtle("square")
        new_snake_segment.color("white")
        new_snake_segment.penup()
        new_snake_segment.setpos(start_pos_x, start_pos_y)
        self.segments.append(new_snake_segment)
        if len(self.segments) < 4:
            self.start_pos_x -= MOVE_DISTANCE

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.start_pos_x = 0
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    def move(self):
        for seg_i in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_i].goto(self.segments[seg_i - 1].pos())
        self.segments[0].fd(MOVE_DISTANCE)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


