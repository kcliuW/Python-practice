# MC q3
i=1
while i <105:#迴圈條件式
    i += 2   #調整變數增減值
print(i)

# MC q4
sum=0	
count = 0 #計數器
while count <= 12:  
   sum += count #將3的倍數累加
   count += 3
print( sum) #輸出累加結果

# Practice Q2
x = "13579"
for i in x:
    print(i,end='\n')

# Practice Q3
y = ['Love', 'Happy', 'Money']
for i in y:
    print(i)

# Practice Q4
for x in range(1,5,2):
    print(x, end=" ")
print()

# Practice Q5
product=1
for i in range(1,11,3): 
    product*=i
print(product)

# Practice Q6
n=53179
while n!=0:  
    print("%d" %(n%10),end='') 
    n//=10


