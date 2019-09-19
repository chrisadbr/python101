secret_number = 7 #assigned wiining number
number_of_guesses = 3 #total number of guesses
guess_count = 0

name = input('Enter your name: ')
#Initiate a loop
while guess_count < number_of_guesses:
    guess_number = int(input('Enter the guess number: '))
    guess_count += 1

    #Checking if user guessed right
    if guess_number == secret_number:
        print("\n" + name.title() + ", you are a winner!")
        break     #Terminates a loop when player wins

else:
    # message when player looses
    print(name.title() + ",  sorry you didn't win")