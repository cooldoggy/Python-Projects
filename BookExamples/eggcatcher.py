from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

canvaswidth=800
canvasheight=400
root=Tk()
c=Canvas(root, width=canvaswidth, height=canvasheight, background='deep sky blue')
c.create_rectangle(-5, canvasheight- 100,canvaswidth + 5, canvasheight + 5, fill='sea green', width=0)
c.create_oval(-80,-80,120,120,fill='orange',width=0)
c.pack()
colorcycle=cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])
eggwidth=45
eggheight=55
eggscore=10
eggspeed=500
egginterval=4000
difficultyfactor=0.95
catchercolor='blue'
catcherwidth=100
catcherheight=100
catcherstartx=canvaswidth / 2 - catcherwidth/ 2
catcherstarty=canvasheight - catcherheight -20
catcherstartx2=catcherstartx + catcherwidth
catcherstarty2 = catcherstarty + catcherheight
catcher = c.create_arc(catcherstartx, catcherstarty, \
                       catcherstartx2, catcherstarty2, start=200, extent=140, \
                       style='arc', outline=catchercolor, width=3)
gamefont=font.nametofont('TkFixedFont')
gamefont.config(size=18)
score=0
scoretext=c.create_text(10,10, anchor='nw', font=gamefont, fill='darkblue', text='Score: '+ str(score))
livesremaining=3
livestext=c.create_text(canvaswidth -10, 10, anchor='ne', font=gamefont, fill='darkblue', text='Lives: ' + str(livesremaining))
eggs=[]
def create_egg():
    x=randrange(10,740)
    y=40
    newegg=c.create_oval(x,y, x + eggwidth, y + eggheight, fill=next(colorcycle), width = 0)
    eggs.append(newegg)
    root.after(egginterval, create_egg)
def move_eggs():
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        c.move(egg, 0, 10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    root.after(eggspeed, move_eggs)
