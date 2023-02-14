obj = '''Hello World my dear
I am William Liu
How old are you
'''

fn = open("books.txt", "w")
fn.write(obj)
fn.close()

file = open("books.txt","r")
abc = file.read()
xyz = str(abc).split(' ')
maxword = max(xyz, key=len)
print(maxword)
file.close()