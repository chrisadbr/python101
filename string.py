#Program that elaborate the uses of strings

first_name = 'Christian'    #assign value to a variable name
last_name = 'Brown'     #assign value to a variable

#printing part of the string
print(first_name[0:5] + ' ' + last_name)

#counting the number of characters
print(len(first_name))

#Convert variable to an uppercase letter
print(first_name.upper() + ' ' + last_name.upper())

#Convert variable to lower case letters
print(last_name.lower() + " " + first_name.lower())

#Checking if letters exist in a sentence
stm = "Iam going to see the Santinos tonight"
x = "ing" in stm
print(x)

stm_2 = "Mount Kilimanjaro"
find_phrase = stm_2.find("welcome")
print(find_phrase)

