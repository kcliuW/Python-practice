# Question 1
# The followings are correct descriptions of "Dictionaries" 
'''
1. Dictionaries can have "lists" as values

2. Dictionaries can have "dictionaries" as values

3. List can have "dictionaries" as elements
'''

# Question 2
nums = [6, 4, 3, 5, 2, 1]
x = 7
nums.remove(nums[2])
nums.append(x)
print(nums[5])

# Question 3
my_list = [1, 2, 3, 4, 5]
print(my_list[4]%3)

# Question 4
string = "edakrak"
list = range(6)
if (type(list)== list):
    print(string[::2], string[1::2], sep="")
else:
    print(string[::-1])

# Question 5
print("I Love coding".replace("coding","sololearn"))