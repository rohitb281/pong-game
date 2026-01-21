from turtle import Turtle, Screen
import random
import math


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.paddle_bounce()

    def increase_speed(self):
        if self.x_move < 0:
            self.x_move -= 0.5
        else:
            self.x_move += 0.5
        if self.y_move < 0:
            self.y_move -= 0.5
        else:
            self.y_move += 0.5
