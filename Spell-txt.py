txt = input("Please input text: ")
def spell(txt):
    if len(txt) == 1:
        print(txt)
        return
    else:
        print(txt[-1])
        return spell(txt[0:-1])

spell(txt)