list1 = [41, 16, 12, 'a', 'b']
print("list1 is: ", list1)
list2 = list1
print("list2 is: ", list2)
list2.append(3)
print("list2.append(3)is: ",list2)

list3 = list2
print("list3 is: ", list3)
list3.insert(1, 55)
print("list3.insert(1, 55)is: ",list3)
#print('\n')

print("Because list1 = list2 = list3. Therefore, list1 is equals to: ",list1)