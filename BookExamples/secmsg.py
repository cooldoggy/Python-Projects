from tkinter import messagebox, simpledialog, Tk
import sys
def get_task():
    task = simpledialog.askstring('Task?', 'Encrypt or Decrypt?')
    return task
def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message.')
    if message == None:
        sys.exit()
    return message
def iseven(number):
    return number % 2 == 0
def geteven(message):
    evenletters=[]
    for counter in range(0, len(message)):
        if iseven(counter):
            evenletters.append(message[counter])
    return evenletters
def getodd(message):
    oddletters=[]
    for counter in range (0, len(message)):
        if not iseven(counter):
            oddletters.append(message[counter])
    return oddletters
def swap_letters(message):
    letterlist = []
    if not iseven(len(message)):
        message = message + 'x'
    evenletters = geteven(message)
    oddletters = getodd(message)
    for counter in range(0, int(len(message)/2)):
        letterlist.append(oddletters[counter])
        letterlist.append(evenletters[counter])
    newmessage = ''.join(letterlist)
    return newmessage
def encrypt(message):
    swappedmessage = swap_letters(message)
    encryptedmessage = ''.join(reversed(swappedmessage))
    return encryptedmessage
def decrypt(message):
    unrevmsg = ''.join(reversed(message))
    decryptedmsg = swap_letters(unrevmsg)
    return decryptedmsg
root=Tk()
root.withdraw()
while True:
    task = get_task()
    if task == None:
        sys.exit()
    task = task.capitalize()
    if task == 'Encrypt':
        message = get_message()
        encryptedmsg = encrypt(message)
        messagebox.showinfo('Encrypted!', encryptedmsg)
    elif task == 'Decrypt':
        message = get_message()
        decryptedmsg = decrypt(message)
        messagebox.showinfo('Decrypted!', decryptedmsg)
    else:
        break
root.mainloop()
