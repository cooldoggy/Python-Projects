from tkinter import Tk, simpledialog, messagebox
import sys
def readfromfile():
    with open('capitaldata.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country]= city
def writetofile(country_name, city_name):
    with open('capitaldata.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)
root = Tk()
root.withdraw()
the_world={}
readfromfile()
while True:
    query_country= simpledialog.askstring('Ask the Expert!- Capital Cities', "Type the name of a country:")
    if query_country == None:
    	sys.exit()
    query_country=query_country.capitalize()

    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '.')
    else:
        new_city = simpledialog.askstring('Teach Me!', "I don't know! " + "What is the capital city of " + query_country + '?')
        new_city = new_city.capitalize()
        the_world[query_country] = new_city
        writetofile(query_country, new_city)
        messagebox.showinfo('Thanks!', "Ok! The capital city of " + query_country + " is " + new_city + ".")
root.mainloop()
