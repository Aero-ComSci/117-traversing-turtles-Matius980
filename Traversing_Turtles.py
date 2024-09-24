import turtle as trtl

class TurtleCircle:
    def __init__(self, shapes, colors, start_x=0, start_y=0):
        self.shapes = shapes
        self.colors = colors
        self.start_x = start_x
        self.start_y = start_y
        self.my_turtles = []
        self.current_direction = 0
        self.starting_length = 25
        self.length_increment = 45
        self.create_turtles()

    def create_turtles(self):
        for shape in self.shapes:
            t = trtl.Turtle(shape=shape)
            t.color(self.colors.pop(0))  # Change the color for each shape
            t.goto(self.start_x, self.start_y)
            t.setheading(self.current_direction)
            t.forward(self.starting_length)

            # Update position and direction for the next turtle
            self.start_x += 50
            self.start_y += 50
            self.current_direction += 30

def main():
    turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
    turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

    # Create a TurtleCircle instance
    turtle_circle = TurtleCircle(turtle_shapes, turtle_colors)

    # Create the screen
    wn = trtl.Screen()
    wn.mainloop()

if __name__ == "__main__":
    main()
