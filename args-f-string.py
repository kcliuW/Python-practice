def my_func(x, y=7, *args, **kwargs):
    print(f" x : {x} \n y : {y} \n args : {args} \n kwargs : {kwargs}")

my_func(2,3,4,5,6, a=7, b=8)