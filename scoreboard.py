from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.puntaje_i = 0
        self.puntaje_d = 0
        self.actualizar_puntaje()


    def actualizar_puntaje(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.puntaje_i, align="center", font=("arial", 60, "normal"))
        self.goto(100, 200)
        self.write(self.puntaje_d, align="center", font=("arial", 60, "normal"))

    def punto_i(self):
        self.puntaje_i += 1
        self.actualizar_puntaje()

    def punto_d(self):
        self.puntaje_d += 1
        self.actualizar_puntaje()
