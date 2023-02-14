word = input("Please enter the word: ")

def breakup(word):
    if len(word) > 0:
        yield word
        yield from breakup(word[:-1])

for piece in breakup(word):
    print(piece)