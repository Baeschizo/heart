from os import link
import turtle
from urllib.parse import _ParseResultBase
t = turtle.Turtle()
turtle.title("FOR CRUSH")
screen=turtle.Screen()
screen.bgcolor("white")

#Drawing heart
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)

t.end_fill

#Writing text
t.up()
t.setpos(-110, 140)
t.down()
t.color('red')
t.write("CRUSH BACK MOKO:(", font=("Verdana", 15, "bold"))

t.ht()

link("https://media1.tenor.com/images/51f904d3b8789dd5131ce97cc4be8249/tenor.gif?itemid=7589229")



turtle.mainloop()