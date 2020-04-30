def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct Answer!!')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again.')
            attempt = attempt + 1
    if attempt == 3:
        print('The correct answer is a ' + answer + ".")
score = 0
print('Guess The Animal!')
guess1 = input("Which bear lives at the North Pole?")
check_guess(guess1, 'polar bear')
guess2 = input("Which is the fastest land animal?")
check_guess(guess2, "cheetah")
guess3 = input("Which is the largest animal?")
check_guess(guess3, "blue whale")
guess4 = input('Which animal is an elephant scared of? \n A) A snake \n B) A Cat \n C) A Mouse \n D) A Bat \n Please Answer with A,B,C, or D.')
check_guess(guess4, "C")
if score == 4:
    print('Congratulations! You Scored '+ str(score) + "!")
else:
    print('You scored ' + str(score) + ".")
pause = input("Press Enter to end the program.")
