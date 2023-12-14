#Made by: Gabrielli Danker        December 14/2023

import turtle

t= turtle.Turtle()

turtle.title("For boyfriend") #titulo da janela

screen= turtle.Screen()
screen.bgcolor("black") #cor de fundo da janela
t.color("red") #cor da flecha para fazer o coração

#Centralizando o coração no meio da janela
t.penup()
t.goto(0, -130)  
t.pendown()

t.fillcolor("red") #cor do coração
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(100)
t.end_fill()

#Centralizando a escrita "I LOVE YOU" para o meio do coração
t.penup()
t.goto(0, 10)  
t.pendown()

#Criando a escrita no coração
t.color("white")
t.write("I LOVE YOU", font=("Courier New", 20), align="center")

t.hideturtle()
turtle.mainloop()