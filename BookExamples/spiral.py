import turtle as t
from itertools import cycle
colors= cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
def draw_circle(thick, size, angle, shift):
    t.hideturtle()
    t.pensize(thick)
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(thick,size + 5, angle + 1, shift +1)
print("Please respond to the following questions with only integers or respond default for default settings.")
def get_size():
    size = input("What size do you want the circles to be?")
    if size == 'default':
        size = 30
    return size
def get_thick():
    thick = input("How thick do you want the circles to be?")
    if thick == 'default':
        thick = 4
    return thick
def get_angle():
    angle = input("What angle do you want the circles to shift?")
    if angle == 'default':
        angle = 0
    return angle
def get_shift():
    shift = input("How much would you like the circles to shift forward?")
    if shift == 'default':
        shift = 1
    return shift
size = get_size()
thick = get_thick()
angle = get_angle()
shift = get_shift()
t.bgcolor('black')
t.speed(10)
t.pensize(4)
draw_circle(int(thick), int(size), int(angle), int(shift))