from random import randint
import turtle

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def falls_in_rect(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
            and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False
        
    def distance_from_point(self, x, y):
        return ((self.x - x) **2 + (self.y - y) **2) **0.5
    
class Rectangle():
    
    def __init__(self, point1:Point, point2:Point):
        self.point1 = point1
        self.point2 = point2
        
    def area(self):
        height = self.point1.x - self.point2.x
        width = self.point1.y - self.point2.y
        return height * width

## A special rectangle for our turtle drawing
class TurtleRect(Rectangle):
    
    def draw(self, canvas):
        turtle.setup(600, 500)
        canvas = turtle.Turtle()
        canvas.speed(3.5)

        canvas.up()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.down()
        
        for i in range(2):
            canvas.forward(self.point2.x - self.point1.x)
            canvas.left(90)
            canvas.forward(self.point2.y - self.point1.y)
            canvas.left(90)
        canvas.hideturtle()
        
class TurtlePoint(Point):
    
    def draw(self, canvas, size=5, color='blue'):
        canvas.up()
        canvas.goto(self.x, self.y)
        canvas.down()
        canvas.dot(size, color)


## Guessing Game ##
# while True:

turt_rect = TurtleRect(Point(randint(10, 100), randint(10, 100)), Point(randint(100, 200), randint(100, 200)))

print(f"Rectangle Coordinates: ({turt_rect.point1.x},{turt_rect.point1.y}),({turt_rect.point2.x},{turt_rect.point2.y})")

# input from the user
user_point = TurtlePoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input('Guess Rectangle Area: '))

if user_point.falls_in_rect(turt_rect):
    print("Your guess is True")
else:
    print("Your guess is False")
    
print('area is True!') if user_area == turt_rect.area() else print('area is False by', abs(turt_rect.area() - user_area), 'Correct area is', turt_rect.area())

myturtle = turtle.Turtle()
turt_rect.draw(myturtle)
user_point.draw(myturtle)
turtle.done()

    # Quit program
    # if input("your want to continue? ") == 'n':
    #     break