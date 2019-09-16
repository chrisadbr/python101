import random
#Addition of two numbers
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

print("The sum is " + str(num1 + num2))
print("The difference is " + str(num1 - num2))
print("Multiplication of two numbers " + str(num1 * num2))
print("Division of two numbers is " + str(round(num1 / num2, 2)))

#Dealing with exponents
exponent = num1 ** num2
print("\nThe exponent: " + str(round(exponent, 2)))

#how python follows BODMAS
ans = (num1 + num2 * 4)  / 6 + num2
print("\nThe answer following BODMAS rules is: " + str(round(ans, 2)))

#complex numbers
d = complex(num1, num2)
a = abs(d)
print("Complex number equivalent ",str(d))
print("Magnitude = " + str(round(a, 2)))

#printing random numbers
y = random.randrange(1, 12)
print("\nThe current running number is " + str(y))