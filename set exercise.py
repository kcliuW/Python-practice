'''mc 1'''
s=[i for i in range(5,18,3)]
print(s)

'''mc2'''
list=('2018', 176, 80, '台灣省新北市') # it is a invalid list

'''mc3'''
num = [[25,58,66], [21,77,36]]
print(num[1][1])

'''mc4'''
word = ["red", "yellow", "green"]
word.sort()
print(word)

'''mc5'''
word = ["red", "yellow", "green", "white"]
print(len(word))

'''PQ1'''
a = [i+5 for i in range(10,15)]
print(a)

'''PQ2'''
list = [1,3,5,7,9,7,5,3,1]
print(list[4:8])
print(list[-2:])

'''PQ3'''
num = [[[1,8,77], [6,1,4], [5,3,4]],[[2,8,0], [2,5,3], [7,1,3]]]
print(num[0][0])
print(num[0][0][0])

'''PQ4'''
L = [51,82,77,48,35]
del L[2]
del L[3]
print(L)

'''PQ5'''
word = ["1", "3", "5", "7"]
word.pop()
print(word)
word.pop()
print(word)

'''PQ6'''
y = (1,2,6)*3
print(y)

'''PQ7'''
dic = {'name':'Python 程式設計', 'author':'許志峰'}
dic['name'] = 'Python 程式設計第二版'
print(dic)

'''PQ8'''
friendA = {"Andy", "Axel", "Michael", "Julia"}
friendB = {"Peter", "Axel", "Andy", "Tom"}
print(friendA & friendB)