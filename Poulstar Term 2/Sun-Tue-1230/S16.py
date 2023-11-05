# https://join.skype.com/HPOq6va7VZZH
from turtle import circle,done,fd,lt
from random import choice,randint


def square(district):
    for i in range(4):
        fd(distance=district)
        lt(90)

def triangle(district):
    for i in range(3):
        fd(distance=district)
        lt(120)

def rectangle(district_x,district_y):
    for i in range(2):
        fd(distance=district_x)
        lt(90)
        fd(distance=district_y)
        lt(90)

shapes = ["circle","square","triangle","rectangle"]

start = input("Hi,Welcome to shape drawer!\nWould you like to draw a shape?(Y/N)\n>> ").lower()
if start == "y":

    while True:
        selected_shape = choice(shapes)
        if selected_shape == "circle":
            circle(radius=randint(50,150))
        elif selected_shape == "square":
            square(district=randint(50,150))
        elif selected_shape == "triangle":
            triangle(district=randint(50,150))
        elif selected_shape == "rectangle":
            rectangle(district_x=randint(50,150),district_y=randint(50,150))
        again = input("Continue?(Y/N)\n>> ").lower()
        if again == "y":
            continue
        elif again == "n":
            print("Have a nice day!\nAnd stay away from Taha '**Twice**'!")
            break

else:
    print("Have a nice day!\nAnd stay away from Taha!")
