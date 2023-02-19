'''
Given a sentence as input, calculate and
output the average word length of that
sentence.

To calculate the aveerage word length, you
need to divide the sum of all word lengths by
the number of words in the sentence.
'''

text = input("Please enter the sentence: ")
words = text.split()
a = len(words)
print(a)
counter = 0
for i in words:
    counter += len(i)
print(counter)
average = counter/a
print(round(average, 2))