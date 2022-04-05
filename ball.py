from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.velocidad = 0.1

    def move(self):
        n_x = self.xcor() + self.x_move
        n_y = self.ycor() + self.y_move
        self.goto(n_x, n_y)

    def rebotar_y(self):
        self.y_move *= -1
        self.velocidad *= 0.9

    def rebotar_x(self):
        self.x_move *= -1
        self.velocidad *= 0.9

    def reiniciar_posicion(self):
        self.goto((0, random.randint(-280, 280)))
        self.rebotar_x()
        self.velocidad = 0.1
