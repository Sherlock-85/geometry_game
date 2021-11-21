import math
import turtle
from random import randint

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
                and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return math.sqrt((self.x - point.x)** 2 + (self.y -point.y) **2)

class GuiPoint(Point):

    def draw(self, canvas, size= 5, color='purple'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def find_area(self, area_guess):
        if area_guess == (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y):
            print( f'Your guess of {area_guess} was correct! The area of the rectangle is:', \
                   (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y))
        else:
            print(f"Your guess of {area_guess} was incorrect! Your area guess was off by:", \
                   (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)-area_guess)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.pendown()
        canvas.forward(self.upright.x-self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y-self.lowleft.y)
        canvas.left(90)
        canvas.forward(self.upright.x-self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y-self.lowleft.y)
        # refers to turtle library



# Create a rectangle object
rectangle = GuiRectangle(Point(randint(0, 199), randint(0, 199)), Point(randint(200, 400), randint(200, 400)))

print("Rectangle Coordinates: ", rectangle.lowleft.x, ",", rectangle.lowleft.y, "and",
      rectangle.upright.x, ",", rectangle.upright.y)

# Get the point and guess the area from user
user_point = GuiPoint(float(input("Guess X: ")),
                   float(input("Guess Y: ")))
user_area = float(input("Guess the area of the rectangle:"))

# Print out the results
print("Your point was inside rectangle:",
user_point.falls_in_rectangle(rectangle))
rectangle.find_area(user_area)

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()