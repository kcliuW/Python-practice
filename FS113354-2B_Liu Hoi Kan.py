n = int (input ("= "))
pattern = input ("pattern = ")
for i in range (1, n + 1):
    for j in range (0, i ):
        print (pattern, end = "")
    print ("")

for i in range (1, n + 1):
    for j in range (n, i, -1):
        print (pattern, end = "")
    print ("")