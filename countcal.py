from tkinter import Tk, Canvas
from datetime import date, datetime
root = Tk()
c = Canvas(root, width = 800, height = 800, bg = 'black')
c.pack()
c.create_text(100, 50, anchor='w', fill = 'green', font = '"Comic Sans MS" 28 bold underline', text = 'My Countdown Calendar')
root.mainloop()