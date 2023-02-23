friendA = {"Andy", "Axel", "Michael", "May"}
friendB = {"Peter", "Axel", "Andy", "Julia"}
print(friendA & friendB)  # Intersection : Elements in Both A and B
print(friendA | friendB)  # Union : Elements in A or B
print(friendA - friendB)  # Difference : Elements in A but not in B
print(friendB - friendA)  # Difference : Elements in B but not in A
print(friendA ^ friendB)  # Exclusion : Elements not in Both A and B

set1 = {5,6,7,3,9}
print(set1)
set2 = {8,5,"happy","1235",(3,2,5),('a','b')}
print(set2)
# set3 = {8,5,"happy","1235",[3,2,5],('a','b')} # No hashable because set require immutable item
# print(set3)

# add()/remove()
friend = {"Andy", "Axel", "Michael", "May"}
friend.remove("Andy")
print(friend)

# update()
friend = {"Andy", "May", "Axel"}
friend.update({"Andy", "May", "John", "Michael"})
print(friend)

# element In testing
friend = {"Andy", "May", "Axel"}
print("Mike" in friend) # 輸出 False