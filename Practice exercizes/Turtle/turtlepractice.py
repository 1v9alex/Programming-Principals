import turtle
import random

# get the size of the screen
screen = turtle.Screen()
screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2

# create a turtle and set its speed
t = turtle.Turtle()
t.speed(0)

# define a function to move the turtle randomly
def move():
    # generate a random angle and distance
    angle = random.randint(0, 360)
    distance = random.randint(10, 50)
    
    # move the turtle in the random direction
    t.right(angle)
    t.forward(distance)
    
    # choose a random color and set the turtle's pen color
    color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])
    t.pencolor(color)

    # choose a random fill color and begin a fill
    fill_color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])
    t.fillcolor(fill_color)
    t.begin_fill()

    # draw a polygon with a random number of sides
    sides = random.randint(3, 8)
    for i in range(sides):
        t.forward(50)
        t.right(360 / sides)

    # end the fill
    t.end_fill()

    # leave a dot at the current position
    t.dot(10)

    # leave an impression of a turtle shape at the current location
    t.stamp()

    # keep the turtle within the screen bounds
    x, y = t.position()
    if x > screen_width:
        t.setx(screen_width)
        t.right(180 - angle)
    elif x < -screen_width:
        t.setx(-screen_width)
        t.right(180 - angle)
    if y > screen_height:
        t.sety(screen_height)
        t.right(360 - angle)
    elif y < -screen_height:
        t.sety(-screen_height)
        t.right(360 - angle)

    # choose a random background color and set the screen's background color
    bg_color = random.choice(["white", "black", "gray", "red", "orange", "yellow", "green", "blue", "purple"])
    turtle.Screen().bgcolor(bg_color)

# listen for key presses
turtle.listen()

# when the "space" key is pressed, move the turtle
turtle.onkey(move, "space")

# when the "Escape" key is pressed, exit the program
turtle.onkey(turtle.bye, "Escape")

# move the turtle to a random position within the screen bounds
x = random.randint(-screen_width + 50, screen_width - 50)
y = random.randint(-screen_height + 50, screen_height - 50)
t.up()
t.goto(x, y)
t.down()

# set the turtle's shape to a random shape
shapes = ["arrow", "turtle", "circle", "square"]
shape = random.choice(shapes)
t.shape(shape)

# set the turtle's pen color to a random color
color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])
t.pencolor(color)

# set the turtle's fill color to a random color
fill_color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])
t.fillcolor(fill_color)

# start the game
turtle.mainloop()