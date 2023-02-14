# Question 1
a = [3, 2, 1]
b = sorted(a)
a.insert(0,1)
print(a)
print(b)
print(b[1])

# Question 2
lst = [1,2,3,4,5]
index = min(max(False, -3, -4),2 ,3, 4)
print(lst[index])

# Question 3
m = [1,2,3,4,5]
n=[]
x=0
for x in range(m[x]):
    n.append(m[x])
print(n)

# Question 4
l = [1, 4, 5]
s = 0
for n in l:
    s += n
print(s)

# Question 5
i, j = 5, 0
test = i**j < 0
print(test)
answ = (0,1)[test]
print(answ)