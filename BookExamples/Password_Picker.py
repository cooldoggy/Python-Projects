import random
import string
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange','yellow'
              ,'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']
nouns = ['apple', 'toaster', 'dinosaur', 'ball', 'goat', 'dragon', 'hammer',
         'duck', 'panda']
colors = ['blue', 'green', 'yellow', 'indigo', 'red', 'brown', 'violet', 'purple', 'orange', 'black']
print("Welcome to Password Picker!")
while True:
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
        color = random.choice(colors)
        password = adjective + noun + color + str(number) + special_char
        print('Your new password is: %s' % password)
    repeat = input('Would you like more passwords? (Y/N?): ')
    if repeat == 'n':
        break