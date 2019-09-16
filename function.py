#Program that counts the number of capital and small letters
def get_name(username):
    cap_letters = 0
    low_letters = 0
    length = len(username)

    while length > 0:
        #Checks for the number of capital letters in a phrase
        if username[length - 1].isupper():
            cap_letters += 1

        #Checks for the number of small letters in a phrase
        if username[length - 1].islower():
            low_letters += 1
        length -= 1

    print("There are " + str(cap_letters) + " capital letters")
    print("There are " + str(low_letters) + " small letters")


name = input('Please enter your name: ')
get_name(name)
