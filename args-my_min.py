def my_min(x, *args):
    if x < min(args):
        return x
    else:
        return min(args)

print(my_min(8, 13, 4, 42, 120, 7) )

# Alternative method #
def my_min1(*args):
    return min(args)

print(my_min1(8,13,4,42,120,7))