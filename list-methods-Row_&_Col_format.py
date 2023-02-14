methods=[i for i in dir([]) if i[0].islower()]
w=str(len(max(methods,key = len))+2)
fmt = ('{:'+w+'s}')*3

for fn in zip(*[iter(methods+[''])]*3):
    print(fmt.format(*fn))