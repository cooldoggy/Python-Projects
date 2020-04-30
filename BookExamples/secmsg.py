from tkinter import messagebox, simpledialog, Tk
def get_task():
    task = simpledialog.askstring('Task?', 'Encrypt or Decrypt?')
    return task
def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message.')
    return message
def iseven(number):
    return number % 2 == 0
def geteven(message):
    evenletters=[]
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letter
root=Tk()
root.withdraw()
while True:
    task = get_task()
    task = task.capitalize()
    if task == 'Encrypt':
        message = get_message()
        messagebox.showinfo('Encrypt This Message?', message)
    elif task == 'Decrypt':
        message = get_message()
        messagebox.showinfo('Decrypt This Message?', message)
    else:
        break
root.mainloop()
