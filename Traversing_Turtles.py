import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

class TurtleCircle:
    def __init__(self, shape, color):
        self.turtle = trtl.Turtle(shape=shape)
        self.turtle.penup()
        self.turtle.color(color)
        self.turtle.pensize(2)

    def move_and_draw(self, startx, starty, startDir, forwardLength):
        self.turtle.goto(startx, starty)
        self.turtle.pendown()
        self.turtle.setheading(startDir)
        self.turtle.forward(forwardLength)
        self.turtle.right(45)  # Turn right to form the next side of the octagon

def main():
    startx = 0
    starty = 0
    startDir = 0
    forwardLength = 100

    for i in range(6):  # Loop to create 8 sides of the octagon
        shape = turtle_shapes[i % len(turtle_shapes)]
        color = turtle_colors[i % len(turtle_colors)]
        turtle_obj = TurtleCircle(shape, color)
        turtle_obj.move_and_draw(startx, starty, startDir, forwardLength)
        startx = turtle_obj.turtle.xcor()
        starty = turtle_obj.turtle.ycor()
        startDir += 45  # Increment the direction to form the next side of the octagon

    wn = trtl.Screen()
    wn.mainloop()

# Create a turtle object 
t = trtl.Turtle()

# Function to get coordinates on click
def get_coordinates(x, y):
    print(f"You clicked at ({x}, {y})")

# Capture click events to get coordinates
trtl.onscreenclick(get_coordinates)

if __name__ == "__main__":
    main()
