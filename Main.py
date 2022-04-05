from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
import time
from scoreboard import Scoreboard

pantalla = Screen()

pantalla.setup(width=800, height=600)
pantalla.bgcolor("black")
pantalla.title("A.C.A.B. Pong")
pantalla.tracer(0)

raqueta_d = Paddle((380, 0))
raqueta_i = Paddle((-390, 0))
pelota = Ball((0, random.randint(-280, 280)))
puntaje = Scoreboard()

pantalla.listen()
pantalla.onkey(raqueta_d.go_up, "Up")
pantalla.onkey(raqueta_d.go_down, "Down")
pantalla.onkey(raqueta_i.go_up, "w")
pantalla.onkey(raqueta_i.go_down, "s")

jugando = True
while jugando:
    time.sleep(pelota.velocidad)
    pantalla.update()
    pelota.move()
    if pelota.ycor() > 280 or pelota.ycor() < -280:
        pelota.rebotar_y()

    if pelota.distance(raqueta_d) < 50 and pelota.xcor() > 360 or \
            pelota.distance(raqueta_i) < 50 and pelota.xcor() < -370:
        pelota.rebotar_x()

    if pelota.xcor() > 400:
        pelota.reiniciar_posicion()
        puntaje.punto_i()

    if pelota.xcor() < -400:
        pelota.reiniciar_posicion()
        puntaje.punto_d()

pantalla.exitonclick()
