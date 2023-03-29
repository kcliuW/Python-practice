''' Task '''

# Write a program in Python language that an input from the user. MCSR - 166
# Let the programme output True if the following conditions are met, else, False. 
# The condition is if a string is entered the last letter of a word should be the beginning of the next word in the string. 
# For example, sample input is"this string got the example", then the sample output is "True".

'''
 Answer
'''
# You can create a Python program to achieve this by using the input() function 
# to get input from the user and then checking if the last letter of a word is the same as the first
# letter of the next word. Here's an example of how you can do this:

def check_words_order(string):
    words = string.split()
    for i in range(len(words)-1):
        if words[i][-1] != words[i + 1][0]:
            return False
    return True


user_input = input("Enter a string: ")
result = check_words_order(user_input)
print(result)

# This program defines a function, check_words_order, which takes a string as input,
# splits it into words, and checks if the last letter of a word is the same as the 
# first letter of the next word. The program then takes input from the user and uses 
# this function to determine if the input string meets the condition specified.