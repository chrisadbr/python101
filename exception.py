#prompt a user for a name
name = input('Enter your name: ')
try:
    #prompt user for their age
    age = int(input('Enter your age: '))
    #checks user's age
    if age > 20:
        print(name.title() + ", you are old enough to drive now")
    else:
        print(name.title() + ", you are not allowed to drive")

#Handle errors if occurs
except ValueError:
    print('Enter a valid age please')
