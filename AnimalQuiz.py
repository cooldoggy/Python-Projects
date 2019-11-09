def check_guess(guess, answer):
    global score
    if guess == answer:
        print("Correct Answer!!")
        score = score + 1
score = 0
print('Guess The Animal!')
guess1 = input("Which bear lives at the North Pole?")
