'''
Problem : You need to make a program that counts the number of 
vowels in a given text.
The vowels are "a", "e", "i", "o", "u".

Take a string as input and output the number 
of vowels.
'''

line = str(input("Please enter a string: "))
vowels = ("a", "e", "i", "o", "u")
count = 0
for x in line:
    if x in vowels:
        count += 1
print(count)

# Examples 2

line = str("python is great, its awesome!")
vowels = ("a","e","i","o","u")
count = 0
for x in line:
    if x in vowels:
        count +=1
print(count)

# Single line example 1
#print(sum(c in'aeiou'for c in input().lower()))

# Single line example 2
#print(sum(map(input().count('a','e','i','o','u')))) 