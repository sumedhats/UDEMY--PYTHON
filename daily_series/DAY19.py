import turtle

# Set up screen
screen = turtle.Screen()
screen.title("Heart Turtle")
screen.bgcolor("white")

# Register the heart shape from gif file
screen.addshape("heart.gif")

# Create turtle
viki_the_turtle = turtle.Turtle()
viki_the_turtle.shape("heart.gif")  # Use the custom shape
viki_the_turtle.penup()
viki_the_turtle.goto(0, 0)
viki_the_turtle.stamp()  # Stamp the heart shape on screen

turtle.done()
