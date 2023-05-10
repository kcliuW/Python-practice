'''
Question 1
'''
n = "89"
n = n.zfill(6)
print(n)


'''
Question 2
'''

rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows + 1):
    for space in range(1, (rows-i)+1):
        print(end=" ")
    while k!=(2*i-1):
        print(" *", end="")
        k += 1
    k = 0
    print() 
        
'''
Question 3
'''

list1 = [14, 6, 12, 17, 1, 8]
list1[2:].extend([4,6,7])
print(list1[::-1])

'''
Question 4
'''

list1=[15, 16, 12, 55, 8]
list2=list1[:3]*2 + list1[1:2]
print(list2)

'''
Question 5
'''

list1 = [11, 16, 11, 'a', 'b', 'a', 'b']
result = list1[1:5:2] + list(set(list1))
print(set(result))
