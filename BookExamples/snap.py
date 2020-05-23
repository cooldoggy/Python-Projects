import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL
def nextshape():
    global shape
    global previouscolor
    global currentcolor
    previouscolor = currentcolor
    c.delete(shape)
    if len(shapes) > 0:
        shape=shapes.pop()
        c.itemconfigure(shape, state=NORMAL)
        currentcolor= c.itemcget(shape, 'fill')
        root.after(1000, nextshape)
    else:
        c.unbind('q')
        c.unbind('p')
        if player1score > player2score:
            c.create_text(200,200, text="Winner: Player 1!!!")
        elif player2score > player1score:
            c.create_text(200,200, text="Winner: Player 2!!!")
        else:
            c.create_text(200,200, text='Draw!')
        c.pack()
def snap(event):
    global shape
    global player1score
    global player2score
    valid = False
    c.delete(shape)
    if previouscolor==currentcolor:
        valid=True
    if valid:
        if event.char=='q':
            player1score= player1score +1
        else:
            player2score= player2score +1
        shape = c.create_text(200,200, text = 'SNAP! You scored a point!')
    else:
        if event.char=='q':
            player1score=player1score - 1
        else:
            player2score = player2score -1
        shape = c.create_text(200,200,text='Wrong! You lost a point!')
    c.pack()
    root.update_idletasks()
    time.sleep(1)
root=Tk()
root.title('Snap')
c=Canvas(root, width=400, height=400)
shapes=[]

#drawing code
circle = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
shapes.append(circle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='black', fill='black', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='red', fill='red', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN)
shapes.append(rectangle)
square=c.create_rectangle(35,20,365,350,outline='black', fill='black',state=HIDDEN)
shapes.append(rectangle)
square=c.create_rectangle(35,20,365,350,outline='red', fill='red',state=HIDDEN)
shapes.append(rectangle)
square=c.create_rectangle(35,20,365,350,outline='green', fill='green',state=HIDDEN)
shapes.append(rectangle)
square=c.create_rectangle(35,20,365,350,outline='blue', fill='blue',state=HIDDEN)
shapes.append(rectangle)

c.pack()
random.shuffle(shapes)
shape = None
previouscolor=''
currentcolor=''
player1score=0
player2score=0
root.after(3000,nextshape)
c.bind('q', snap)
c.bind('p', snap)
c.focus_set()

root.mainloop()
