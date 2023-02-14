obj = '''Hello World my dear
I am William Liu
How old are you
'''

fn = open("books.txt", "w")
fn.write(obj)
fn.close()

file = open("books.txt","r")
abc = file.readlines()
for line in abc:
    print(str(line[:1])+str(len(line.rstrip())))
file.close()