import turtle

def draw_heart():
    turtle.fillcolor("#800000")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def write_message(name):
    turtle.penup()
    turtle.goto(10, 100)
    turtle.pendown()
    turtle.color("white")
    turtle.write(f"Happy Late Valentine\n{name}!", align="center", font=("Montserrat", 12, "bold"))

turtle.speed(3)

draw_heart()
write_message("Aira")  # Replace with a specific name

turtle.hideturtle()
turtle.done()