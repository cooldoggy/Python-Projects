from tkinter import HIDDEN, NORMAL, Tk, Canvas, simpledialog
import random
def toggle_eyes():
    current_color = c.itemcget(eyeleft, "fill")
    new_color = c.body_color if current_color == "white" else 'white'
    current_state= c.itemcget(pupilleft, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupilleft, state=new_state)
    c.itemconfigure(pupilright, state=new_state)
    c.itemconfigure(eyeleft, fill=new_color)
    c.itemconfigure(eyeright, fill=new_color)

def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)
def togglepupils():
    if not c.eyes_crossed:
        c.move(pupilleft, 10, -5)
        c.move(pupilright, -10,-5)
        c.eyes_crossed=True
    else:
        c.move(pupilleft, -10, 5)
        c.move(pupilright, 10,5)
        c.eyes_crossed=False
def toggletongue():
    if not c.tongue_out:
        c.itemconfigure(tonguetip, state=NORMAL)
        c.itemconfigure(tonguemain, state=NORMAL)
        c.tongue_out=True
    else:
        c.itemconfigure(tonguetip, state=HIDDEN)
        c.itemconfigure(tonguemain, state=HIDDEN)
        c.tongue_out=False
def cheeky(event):
    toggletongue()
    togglepupils()
    hidehappy(event)
    root.after(1000, toggletongue)
    root.after(1000, togglepupils)
    return
def showhappy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheekleft, state=NORMAL)
        c.itemconfigure(cheekright, state = NORMAL)
        c.itemconfigure(mouthhappy, state=NORMAL)
        c.itemconfigure(mouthnormal, state=HIDDEN)
        c.itemconfigure(mouthsad, state=HIDDEN)
        c.happy_level=10
    return
def hidehappy(event):
    c.itemconfigure(cheekleft,state=HIDDEN)
    c.itemconfigure(cheekright,state=HIDDEN)
    c.itemconfigure(mouthhappy,state=HIDDEN)
    c.itemconfigure(mouthnormal,state=NORMAL)
    c.itemconfigure(mouthsad,state=HIDDEN)
    return
def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouthhappy, state=HIDDEN)
        c.itemconfigure(mouthnormal,state=HIDDEN)
        c.itemconfigure(mouthsad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(5000, sad)
root = Tk()
root.withdraw()
PetName= simpledialog.askstring("Name your pet!","What will you name your pet?")
root.deiconify()
root.title(PetName)
root.resizable(width=False, height=False)
c = Canvas(root,width=400,height=400)
c.configure(bg='dark blue', highlightthickness=0)

#Drawing Code
petcolors=['SkyBlue1', 'tomato','red', 'blue','green','purple','orange','yellow','indigo']
c.body_color=random.choice(petcolors)
body=c.create_oval(35, 20, 365, 350,outline=c.body_color, fill=c.body_color)
earleft = c.create_polygon(75, 90, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
earright= c.create_polygon(255,45,325,10,320,70, outline=c.body_color, fill=c.body_color)
footleft= c.create_oval(65,320,145,360, outline=c.body_color, fill=c.body_color)
footright= c.create_oval(230, 320, 330,360, outline=c.body_color, fill=c.body_color)
eyeleft=c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupilleft=c.create_oval(140,145,150,155, outline='black', fill='black')
eyeright=c.create_oval(230,110,260,170,outline='black', fill='white')
pupilright=c.create_oval(240,145,250,155,outline='black', fill='black')
mouthnormal=c.create_line(170,250,200,272,230,250, smooth=1,width=2 , state = NORMAL)
mouthhappy=c.create_line(170,250,200,282,230,250, smooth=1, width=2, state=HIDDEN)
mouthsad= c.create_line(170,250,200,232,230,250, smooth=1, width=2, state = HIDDEN)
tonguemain=c.create_rectangle(170,250,230,290, outline='red', fill='red', state=HIDDEN)
tonguetip=c.create_oval(170,285,230,300, outline='red', fill='red', state=HIDDEN)
cheekleft= c.create_oval(70,180,120,230, outline = 'pink', fill= 'pink', state = HIDDEN)
cheekright=c.create_oval(280,180,330,230, outline='pink', fill='pink', state=HIDDEN)


c.bind('<Motion>', showhappy)
c.bind('<Leave>', hidehappy)
c.bind('<Double-1>',cheeky)

c.happy_level=10
c.eyes_crossed=False
c.tongue_out=False
root.after(1000, blink)
root.after(5000, sad)
c.pack()
root.mainloop
