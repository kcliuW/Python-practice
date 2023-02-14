def function(name_arg, *args):
    print(name_arg)
    print(args)
    for i in range(len(args)):
        print(args[i],"\t", end="")

function(1,2,3,4,5) 