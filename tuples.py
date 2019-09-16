#Program that prints what a restaurant offers
food_menu = ('potatoes', 'rice', 'pilau', 'banana', 'ugali')
print("\nThis is the original tuple")
print(food_menu)
print("\nOur restaurant currently serves:")

for food in food_menu:
    #replacing menu item with another item
    if food == 'ugali':
        food = "pizza"
    print(food.title())
print("There are " + str(len(food_menu)) + " items in the menu")

#Picking odd numbers and even numbers from a tupple
nums = list(range(1, 21))  #create a list of numbers
nums = tuple(nums)  #convert the list into a tuple

#create a temporary lists to contain odd and even numbers
odd_nums = []
even_nums = []

#Sorting out a list odd numbers and even numbers
for number in nums:
    if number % 2 == 1:
        odd_nums.append(number)
    elif number % 2 == 0:
        even_nums.append(number)

#create a tuple contains odd numbers
odd_nums = tuple(odd_nums)
#create a tuple contains even numbers
even_nums = tuple(even_nums)

print('\nTuple of sorted even numbers:')
print(even_nums)
print('\nTuple contains sorted odd numbers: ')
print(odd_nums)
