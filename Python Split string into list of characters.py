'''
Python | Split string into list of characters
'''
# Method 1: Split a string into a Python list using 'UNPACK(*) method'
            # The act of unpacking involves taking things out, specifically \
            # terables like dictionaries, lists, and tuples.

string = "geeks"
print([*string])

# Method 2: Split a string into a Python list using a 'loop'
            # Here, we are splitting the letters using the native way 
            # using the loop and then we are appending it to a new list.

string = 'geeksforgeeks'
lst = []

for letter in string:
	lst.append(letter)

print(lst)

# Method 3: Split a string into a Python list using 'List Comprehension'

string = "Geeksforgeeks"
letter = [x for x in string]
print(letter)

# Method 4: Split a string into a Python list using a 'list()' typecasting
        # Python provides direct typecasting of strings into a list using Python list().

def split(word):
	return list(word)
	
# Driver code
word = 'geeks'
print(split(word))

# Method 5: Split a string into a Python list using 'extend()'
        # Extend iterates over its input, expanding the list, and adding each member.

string = 'Geeks@for'
lst = []
lst.extend(string)
print(lst)
