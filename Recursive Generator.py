def breakup(word):
    if len(word) > 0:
        yield word
        yield from breakup(word[:-1])

for piece in breakup('Python!'):
    print(piece)