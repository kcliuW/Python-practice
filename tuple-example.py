# Tuple example
t='733254','Andy',178 #  No brackets
tupledata = ('733259', 'Michael', 185) # Named tuple
obj = ("Michaelwave",) # Tuple with one element

# Tuple operations
s=(1,5,8) + (9,4,2)
print(s)

u = (3,5,6)*3
print(u)

tup = (90,43,65,72,67,55)
print(tup[3])
print(tup[-3])
print(tup[1:4])
print(tup[-6:-2])
print(tup[-1:-3])

# Tuple function
# a) sum()
bonus = (900, 580, 850, 480, 800, 1000, 540, 650, 200, 100)
print('所有紅利積點', sum(bonus), ', 平均紅利點數', sum(bonus)/len(bonus))

# b) max(T)
print(max((89,32,58,76)))

# c) min(T)
print(min(89,32,58,76))
