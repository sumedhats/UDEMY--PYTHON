from turtle import Turtle,Screen
viki_the_turtle = Turtle()
viki_the_turtle.shape("turtle")
viki_the_turtle.color("green")
viki_the_turtle.pensize(5)
for _ in range(10):
    viki_the_turtle.pendown()
    viki_the_turtle.forward(5)   
    viki_the_turtle.penup()
    viki_the_turtle.forward(5) 

