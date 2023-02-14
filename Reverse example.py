# Reverse a number as a string
number = float(input("Please enter a number: "))

reversed_number_string = str(number)[::-1]
if type(number) == float:
    reversed_number = float(reversed_number_string)
elif type(number) == int:
    reversed_number = int(reversed_number_string)

print(reversed_number)

# How to Reverse a Number with a While Loop ( Integers only346)
number = int(input("Please enter a number: "))
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(reversed_number)
