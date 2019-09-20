print("Program that displays list of cities:")
#List of cities in Tanzania

cities_tz = ['mbeya', 'dar-Es-Salaam', 'tanga', 'mwanza', 'dodoma', 'arusha']

#Sort the order of cities alphabetically
cities_tz.sort()

#reverse order of the list alphabetically
cities_tz.sort(reverse = True)

#adding one item at the end of the list
cities_tz.append('kigoma')

#removing last item in the list and assign to the new variable
future_city = cities_tz.pop()

#Looping through the list
for city in cities_tz:

    if city == 'mbeya':
        print("\nWelcome to " + city.title())
        print(city.title() + "'s nickname is 'green city'")
        print("Thanks, I had great time visiting " + city.title())

    elif city == 'mwanza':
        print("\nWelcome to " + city.title())
        print(city.title() + "'s nickname is 'rock city'")
        print("Thanks, I had great time visiting " + city.title())

    elif city == 'dodoma':
        print("\nWelcome to " + city.title())
        print(city.title() + "'s nickname is called the 'capital'")
        print("Thanks, I had great time visiting " + city.title())

    elif city == 'arusha':
        print("\nWelcome to " + city.title())
        print(city.title() + "'s nickname is 'chuga'")
        print("Thanks, I had great time visiting " + city.title())

    else:
        print("\nWelcome to " + city.title())
        print("Thanks, I had great time visiting " + city.title())
print("\nThe fast growing town is  " + future_city.title())

#list of numbers from 1 to 9
numbers = list(range(1, 10))
numbers.reverse()
print(numbers)

#display a list of odd numbers from 1 to 15
odd_numbers = list(range(1, 16, 2))
print(odd_numbers)

#list of cubic values 10 to 1
cubes = []
for values in range(1, 11):
    values **= 3
    cubes.append(values)
    cubes.sort(reverse = True)
print("\nList of cubes from 1 to 10:\n" + str(cubes))