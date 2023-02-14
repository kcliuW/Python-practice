def my_func(x, y=7, *args, **kwargs):
    print(x, "in x of type", type(x))
    print(y, "in y (override 7) of type", type(y))
    print(args, "in *args of type", type(args))
    print(kwargs, "in **kwargs of type", type(kwargs))

my_func(1,2,3,4,5,6, a=7, b=8)  