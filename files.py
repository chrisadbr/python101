#reading a file contents from a folder
my_file = 'notes.txt'
guest_file ='guests.txt'
with open(my_file) as nano:
    contents = nano.read()
    print('\nDisplaying contents of the file notes.txt:\n' + contents.rstrip())
print("There are " + str(len(contents)) + " characters in the file notes.txt")

#Program that navigates through a guest list
print('\nProgram that checks the name of the user exists in the file')
with open(guest_file) as my_guests:
    guest_list = my_guests.read()
    print("This is the guest list:\n" + guest_list)

response = input("Do you have more guests to add? Enter Y or N: ")
response = response.upper()

if response == 'Y':

    guest_name = input("Enter the guest's name or q to quit: ")
    guest_name = guest_name.lower()
    while guest_name != 'q':
        # Adding more names to the guests list
        with open(guest_file, 'a') as add_list:
            add_list.write(guest_name)

        guest_name = input("Enter the guest's name or q to quit: ")
        guest_name = guest_name.lower()

check_guest = ' '
for guest in guest_list:
    check_guest += guest

name = input('Please enter your name to check if you are invited: ')
name = name.title()     #formatting the input to match the file contents

#checking if the name is on the list
if name in check_guest:
    print(name + ", welcome to our event")
else:
    print('Sorry ' + name + ' your name is not on the list')


