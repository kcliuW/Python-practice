'''
Question 1
'''

s1 = {10,20,30}
s2 = {50,20,"10"}

s3 = s1.union(s2)
print(s3)

'''
Question 2
'''
class Acc:
    def __init__(self, id):
        self.id = id
        id = 555
        
acc = Acc(111)
print(acc.id)

'''
Question 3
'''
for i in range(10,15,1):
    print(i, end=', ')
    
print('\n')

'''
Question 4
'''
l1 = [x**3 for x in range(4)]
l1 = l1.pop() + 2
print(l1)


'''
Question 5
'''
list1 = [12, 23, 40]
list2 = [12, 23, 40]
 
print(f"1.) 'list1' reversed: "
      f"{list1[::-1]}")

list2.reverse()
print(f"2.) 'list2' reversed: "
       f"{list2}")

print("1.) 'list1' reversed:", list1[::-1])
print("2.) 'list2' reversed:", list2)
