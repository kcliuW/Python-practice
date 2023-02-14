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