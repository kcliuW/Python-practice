# List introduction
list = []   # empty list
score = [98, 85, 76, 64, 100]  # numeric list
info = ['2018', 176, 80, '台灣省新北市']  # mixed list
mixed = ['manager', [58000, 74800], 'labor', [26000, 31000]]

# for loop
data1 = [i for i in range(5,18,21)]
print(data1)

data2 = [i+5 for i in range(10,45)]
print(data2)

# list slicing
list1 = [7, 5, 4, 3, 8, 1, 9, 6]
print(list1 [4:8])
print(list1 [-2:])

word = ['H','O','L','I','D','A','Y']
print(word [:5])
print(word [1:5])
print(word [3:])

'''
x = 'CHINESE'
lista = list((x))
print(lista)
'''

num = [[25, 58, 66],[21, 97, 36]]
print(num[0])
print(num[1][1])

#  list delete
L = [51,82,77,48,35,66,28,46,99]
del L[6]
print(L)

L = [51,82,77,48,35,66,28,46,99]
del L[1:4]
print(L)

print("happy" in ["good", "happy", "please"])

print("sad" not in ["good", "happy", "please"])

# List append
word = ["red", "yellow", "green"]
word.append("blue")
print(word)

# List insert
word = ["red", "yellow", "green"]
word.insert(2,"blue")
print(word)

# List remove
word = ["red", "yellow", "green"]
word.remove("red")
print(word)

# List pop
word = ["red", "yellow", "green"]
word.pop(2)
print(word)

# List sort
word = ["red", "yellow", "green"]
word.sort()
print(word)

# List reverse
word = ["red", "yellow", "green"]
word.reverse()
print(word)

# List length
word = ["red", "yellow", "green"]
print(len(word))