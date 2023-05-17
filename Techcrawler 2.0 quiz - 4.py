# Question 1

mylist = [1,2,3,4,5,6]
blist = []
x = 1
while mylist != blist:
    blist = mylist.copy()
    mylist[x] = mylist[-x]
    x += 1
print(sum(mylist))      # 27
print(mylist)           # [1, 6, 5, 4, 5, 6]
print(blist)            # [1, 6, 5, 4, 5, 6]
                        # 1.[1, 6, 3, 4, 5, 6], 2.[1, 6, 5, 4, 5, 6] 3.[1, 6, 5, 4, 5, 6]
                        
# Question 2
mylist = [1,2,3,4,5,6]
a = mylist[0]
ctr = 0
while True:
    ctr += 1
    b = mylist.pop(0)
    mylist.append(b)
    if mylist[0] == a:
        break
print(ctr)