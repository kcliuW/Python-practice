# Answer 1
data =[
    [23, 11, 5, 14],
    [8, 32, 20, 5]
]
color = input("Please enter your favourite color: ")
eyecolors = ["brown", "blue", "green", "black"]
total = sum(data[0]+data[1])
if color in eyecolors:
    index = eyecolors.index(color)
    p = int((data[0][index]+data[1][index])/total*100)
    print(p)

