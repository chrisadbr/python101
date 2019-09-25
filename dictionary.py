#Dictionary that displays profile of a person
profile = {
    'first_name': 'john',
    'last_name': 'rosan',
    'hobby': 'surfing',
    'age': 20,
    'location': 'dodoma',
    'occupation': 'software developer'
}

#Looping through the dictionary
for keys, value in profile.items():
    print(keys + " => " + str(value).title())

#Looping through the values only
person = ['juma']
for name in profile.values():

    #checking if person's profile exists
    if name in person:
        print("\nHello, " + name.title() + ", do you still live in " + profile['location'].title() + "?")

