import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size


class Drawer:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.turtle.speed(0)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.screen.colormode(255)

    def draw_polygon(self, polygon):
        self.turtle.penup()
        self.turtle.goto(polygon.location[0], polygon.location[1])
        self.turtle.setheading(polygon.orientation)
        self.turtle.color(polygon.color)
        self.turtle.pensize(polygon.border_size)
        self.turtle.pendown()
        for _ in range(polygon.num_sides):
            self.turtle.forward(polygon.size)
            self.turtle.left(360/polygon.num_sides)
        self.turtle.penup()

    def reposition_turtle(self, polygon):
        reduction_ratio = 0.618
        self.turtle.penup()
        self.turtle.forward((polygon.size * (1 - reduction_ratio)) / 2)
        self.turtle.left(90)
        self.turtle.forward((polygon.size * (1 - reduction_ratio)) / 2)
        self.turtle.right(90)
        polygon.location[0] = self.turtle.pos()[0]
        polygon.location[1] = self.turtle.pos()[1]
        polygon.size *= reduction_ratio


choice = input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: ")

drawer = Drawer()

for _ in range(random.randint(20, 30)):
    if choice == "1":
        num_sides = 3
        layer_amount = 1
    elif choice == "2":
        num_sides = 4
        layer_amount = 1
    elif choice == "3":
        num_sides = 5
        layer_amount = 1
    elif choice == "4":
        num_sides = random.randint(3, 5)
        layer_amount = 1
    elif choice == "5":
        num_sides = 3
        layer_amount = 3
    elif choice == "6":
        num_sides = 4
        layer_amount = 3
    elif choice == "7":
        num_sides = 5
        layer_amount = 3
    elif choice == "8":
        num_sides = random.randint(3, 5)
        layer_amount = 3
    elif choice == "9":
        num_sides = random.randint(3, 5)
        layer_amount = random.randint(1, 3)
    else:
        print("ERROR: Invalid choice")
        exit()

    size = random.randint(50, 150)
    orientation = random.randint(0, 90)
    location = [random.randint(-300, 300), random.randint(-200, 200)]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    border_size = random.randint(1, 10)
    polygon = Polygon(num_sides, size, orientation, location, color, border_size)

    for _ in range(layer_amount):
        drawer.draw_polygon(polygon)
        drawer.reposition_turtle(polygon)

turtle.done()