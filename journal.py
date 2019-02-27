# Week 4 Learning Journal
# I was not sure how to go about recording each stage in the development process.

# importing the math module
import math

# implementing distance example from textbook
# adding random values and a result string
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
print("\nThe distance is equal to: " + str(distance(55,72,49,53)) + "\n")

# creating my own function
# assigning 's' for side, and 'h' for the height
# converting the mathematical formula into a python-readable expression
# it is not too overly complicated, but my favorite shape is a Rhombus!
def rhombus(s, h):
    result = (s*h)/2
    return result
s=float(input("Calculate the area of a Rhombus -- \nEnter a number to indicate the side of the Rhombus: "))
h=float(input("Enter a number to indicate the height of the Rhombus: "))
print("The area of the rhombus is: " + str(rhombus(s,h)),"\r"+"\n")

# creating the hypotenuse function
# assigning 'a' and 'b' to the two right triangle legs as arguments as indicated in the formula
# converting the mathematical formula into a python-readable expression
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
# creating a loop for multiple results
while True:
    a=float(input("Calculating the Hypotenuse of a Right Triangle -- \nEnter a number for leg one (3): "))
    b=float(input("Enter a number for leg two (4): "))
    print("The hypotenuse of a right triangle is equal to: " + str(hypotenuse(a,b)),"\r"+"\n")